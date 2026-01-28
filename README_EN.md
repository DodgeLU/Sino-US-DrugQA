# Sino-US-DrugQA

**Sino-US-DrugQA** is a bilingual (Chinese–English) benchmark dataset designed
to evaluate large language models (LLMs) on **cross-jurisdictional pharmaceutical
regulatory reasoning**, with a focus on comparative analysis between **US FDA**
and **China NMPA** regulatory frameworks.

Unlike existing legal or medical benchmarks that focus on monolingual statutory
interpretation or clinical reasoning, Sino-US-DrugQA targets **administrative
regulatory compliance tasks**, requiring models to align and compare
**non-equivalent regulatory systems**.

---

## 🔍 What This Benchmark Evaluates

Sino-US-DrugQA evaluates whether LLMs can:

- Retrieve regulatory requirements within a single jurisdiction
- Perform cross-jurisdictional comparison (e.g., timelines, thresholds, obligations)
- Maintain concept-level alignment across FDA and NMPA systems
- Avoid hallucinated or over-generalized compliance conclusions

This benchmark is intended **for evaluation and research purposes only**, not
for automated regulatory decision-making.

---

## 📊 Dataset Overview

- **Total questions**: 11,871 multiple-choice QA pairs
- **Languages**: English 51.1%, Chinese 48.9%
- **Jurisdictions**: US FDA (CFR Title 21), China NMPA
- **Task types**:
  - Monolingual: 59.1%
  - Comparative: 36.3%
  - Parallel: 4.6%
- **Source documents**:
  - 134 NMPA regulations
  - 195 CFR Title 21 documents

---

## 🧠 Task Types

| Task Type | Description |
| --- | --- |
| Monolingual | Regulatory retrieval within a single jurisdiction |
| Comparative | Explicit comparison across FDA and NMPA requirements |
| Parallel | Equivalent questions for consistency checks |

---

## 🏷 Regulatory Domains (Top 5)

| Domain | Percentage |
| --- | --- |
| Drugs | 40.0% |
| Medical Devices | 23.4% |
| Cosmetics | 14.3% |
| General FDA / Administrative | 12.3% |
| Controlled Substances | 7.1% |

---

## 🤖 Baseline Models Evaluated (Zero-shot)

| Model | Accuracy |
| --- | --- |
| Gemini-3-flash | 84.51% |
| DeepSeek-V3.2 | 80.53% |
| Qwen-3-235B | 80.04% |
| GPT-5.2 | 78.97% |

All evaluations use a standardized zero-shot and five-shot protocol with
temperature set to 0.

---

## 📁 Repository Structure

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

## 🧾 Data Format

Each line in `data/*.jsonl` corresponds to one QA instance:

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

See `DATASET_CARD.md` for full field descriptions.

---

## 📦 Data Splits

- `data/0-shot/`: full dataset and type-specific JSONL files
- `data/5-shot/`: per-type dev/test split (5 examples per type in dev)

---

## 📌 Prompt Template (Zero-shot)

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

---

## 🧪 Evaluation

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

---

## 📜 Data Sources

Regulatory texts are obtained from official public sources:

- NMPA: https://www.nmpa.gov.cn
- eCFR Title 21: https://www.ecfr.gov

---

## ⚠️ Intended Use & Disclaimer

This dataset is intended for:

- Benchmarking LLM regulatory reasoning
- Research on cross-jurisdictional AI alignment
- Error analysis and robustness studies

It is **NOT** intended for:

- Automated regulatory decision-making
- Legal or compliance advice without expert review

---

## 📄 License

This dataset is released under CC BY 4.0. See `LICENSE`.

---

## 📚 Citation

See `CITATION.bib`.
