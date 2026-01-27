import argparse
import json
import os
import re
import time
from typing import Dict, List

import requests

EVAL_SYSTEM_PROMPT = """You are an expert in US (FDA) and Chinese (NMPA) medical regulations. 
You are taking a professional exam. 
Please read the question and choices carefully, then select the best answer.
Output your response in strict JSON format."""

EVAL_USER_PROMPT_TEMPLATE = """
### Question
{question}

### Choices
{choices_str}

### Task
1. Analyze the regulatory context and logic.
2. Select the correct option (A, B, C, or D).
3. Provide a brief reasoning.

### Output Format (Strict JSON)
{{
    "selected_answer": "A",
    "reasoning": "Brief explanation of why the option is correct..."
}}
"""

TYPE_ORDER = ["Comparative", "Monolingual", "Parallel"]


def load_jsonl(path: str) -> List[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append(json.loads(line))
    return data


def format_choices(choices: List[str]) -> str:
    return "\n".join(choices) if isinstance(choices, list) else str(choices)


def format_few_shot_examples(examples: List[dict]) -> str:
    formatted = "Here are some examples:\n\n"
    for ex in examples:
        choices_str = "\n".join(ex["choices"])
        formatted += (
            f"Question: {ex['question']}\n"
            f"Choices:\n{choices_str}\n"
            f"Answer: {ex['answer']}\n\n"
        )
    formatted += "Now, please answer the following question:\n"
    return formatted


def build_prompt(item: dict, few_shot_examples: List[dict]) -> str:
    choices_str = format_choices(item.get("choices", []))
    user_prompt = EVAL_USER_PROMPT_TEMPLATE.format(
        question=item.get("question", ""),
        choices_str=choices_str,
    )
    if few_shot_examples:
        examples_str = format_few_shot_examples(few_shot_examples)
        return examples_str + user_prompt
    return user_prompt


def extract_choice(text: str) -> str:
    if not text:
        return ""
    match = re.search(r"\b([A-D])\b", text.upper())
    return match.group(1) if match else text.strip()[:1].upper()


def call_qwen(prompt: str, api_key: str, model: str, base_url: str, temperature: float, max_tokens: int) -> str:
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "model": model,
        "input": {
            "messages": [
                {"role": "system", "content": EVAL_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        },
        "parameters": {"temperature": temperature, "max_tokens": max_tokens},
    }
    response = requests.post(base_url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["output"]["choices"][0]["message"]["content"]


def build_5_shot_sets(data_root: str) -> Dict[str, Dict[str, List[dict]]]:
    dev_dir = os.path.join(data_root, "5-shot", "dev")
    test_dir = os.path.join(data_root, "5-shot", "test")
    sets = {}
    for t in TYPE_ORDER:
        sets[t] = {
            "dev": load_jsonl(os.path.join(dev_dir, f"{t}.jsonl")),
            "test": load_jsonl(os.path.join(test_dir, f"{t}.jsonl")),
        }
    return sets


def main() -> None:
    parser = argparse.ArgumentParser(description="Qwen evaluation (single model).")
    parser.add_argument("--data-root", default=os.path.join("..", "data"), help="Data root directory")
    parser.add_argument("--shot", type=int, default=0, choices=[0, 5], help="0-shot or 5-shot")
    parser.add_argument("--output", default=os.path.join("..", "results", "qwen.jsonl"), help="Output JSONL")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (reserved)")
    parser.add_argument("--model", default=os.getenv("QWEN_MODEL", "Qwen-3-235B"), help="Model name")
    parser.add_argument("--base-url", default=os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"), help="API base URL")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")
    parser.add_argument("--max-tokens", type=int, default=1024, help="Max tokens")
    args = parser.parse_args()

    api_key = os.getenv("QWEN_API_KEY", "")
    if not api_key:
        raise ValueError("Missing QWEN_API_KEY")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    if args.shot == 0:
        items = load_jsonl(os.path.join(args.data_root, "0-shot", "all.jsonl"))
        workload = [(item, []) for item in items]
    else:
        sets = build_5_shot_sets(args.data_root)
        workload = []
        for t in TYPE_ORDER:
            dev_examples = sets[t]["dev"]
            for item in sets[t]["test"]:
                workload.append((item, dev_examples))

    with open(args.output, "w", encoding="utf-8") as f:
        for idx, (item, few_shot) in enumerate(workload, start=1):
            prompt = build_prompt(item, few_shot)
            raw = call_qwen(prompt, api_key, args.model, args.base_url, args.temperature, args.max_tokens)
            answer = extract_choice(raw)
            gt = str(item.get("answer", "")).strip().upper()
            result = {
                "id": item.get("id"),
                "model": args.model,
                "shot": args.shot,
                "type": item.get("type"),
                "lang": item.get("lang"),
                "ground_truth": gt,
                "model_answer": answer,
                "is_correct": answer == gt,
                "raw_response": raw,
            }
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
            if idx % 100 == 0:
                time.sleep(0.2)


if __name__ == "__main__":
    main()
