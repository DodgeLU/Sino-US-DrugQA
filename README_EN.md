# Sino-US-DrugQA

Sino-US-DrugQA is a bilingual benchmark for evaluating large language models on
cross-jurisdictional pharmaceutical regulation (US FDA vs China NMPA). It is a
multiple-choice QA dataset with monolingual retrieval, cross-jurisdictional
comparison, and parallel consistency tasks.

## Highlights

- 11,871 QA pairs, bilingual (EN/ZH)
- Task types: Monolingual (59.1%), Comparative (36.3%), Parallel (4.6%)
- Sources: 134 NMPA regulations + 195 CFR Title 21 documents
- Models: DeepSeek-V3.2, GPT-5.2, Qwen-3-235B, Gemini-3-flash

## Dataset Statistics (from paper)

### Language

- English: 6,069 (51.1%)
- Chinese: 5,802 (48.9%)

### Domain (Top 5)

- Drugs: 4,752 (40.0%)
- Medical Devices: 2,772 (23.4%)
- Cosmetics: 1,699 (14.3%)
- General_FDA: 1,465 (12.3%)
- Controlled_Substances: 845 (7.1%)

### Zero-shot Accuracy (Overall)

- Gemini-3-flash: 84.51%
- DeepSeek-V3.2: 80.53%
- Qwen-3-235B: 80.04%
- GPT-5.2: 78.97%

## Repository Structure

```
github/
├── data/
│   ├── 0-shot/
│   ├── 5-shot/
│   └── README.md
├── evaluation/
│   ├── deepseek_eval.py
│   ├── gpt_eval.py
│   ├── gemini_eval.py
│   └── qwen_eval.py
├── scripts/
│   ├── run_deepseek.sh
│   ├── run_gpt.sh
│   ├── run_gemini.sh
│   └── run_qwen.sh
├── DATASET_CARD.md
├── CITATION.bib
└── LICENSE
```

## Dataset Format

Each line in `data/*.jsonl` is a JSON object:

```json
{
  "id": "CO_P_00001_001",
  "question": "...",
  "choices": ["A ...", "B ...", "C ...", "D ..."],
  "answer": "A",
  "type": "Comparative",
  "category": "Drugs",
  "lang": "CN",
  "explanation": "...",
  "source_cn": "...",
  "source_us": "..."
}
```

See `DATASET_CARD.md` and `data/README.md` for full field descriptions.

## Data Splits

- `data/0-shot/`: full dataset and type-specific JSONL files
- `data/5-shot/`: per-type dev/test split (5 examples per type in dev)

## Prompt Template (Zero-shot)

```text
### System Prompt
You are an expert in US (FDA) and Chinese (NMPA) medical regulations.
You are taking a professional exam.
Please read the question and choices carefully, then select the best answer.
Output your response in strict JSON format.

### User Prompt
### Question
{question}

### Choices
{choices_str}

### Task
1. Analyze the regulatory context and logic.
2. Select the correct option (A, B, C, or D).
3. Provide a brief reasoning.

### Output Format (Strict JSON)
{
  "selected_answer": "A",
  "reasoning": "Brief explanation of why the option is correct..."
}
```

## Evaluation

```bash
./scripts/run_deepseek.sh
./scripts/run_gpt.sh
./scripts/run_gemini.sh
./scripts/run_qwen.sh
```

Each script targets the official provider endpoint and accepts `SHOT=0|5`:

```bash
SHOT=5 ./scripts/run_deepseek.sh
```

Model names follow the paper:

- DeepSeek-V3.2
- GPT-5.2
- Qwen-3-235B
- Gemini-3-flash

## Data Availability

The benchmark is derived from publicly available regulations:

- NMPA: https://www.nmpa.gov.cn
- eCFR Title 21: https://www.ecfr.gov

## License

This dataset is released under CC BY 4.0. See `LICENSE`.

## Citation

See `CITATION.bib`.
