# Sino-US-DrugQA

**Sino-US-DrugQA** is a bilingual benchmark dataset for evaluating large language models (LLMs) on **cross-jurisdictional pharmaceutical regulation**, with a focus on comparative reasoning between **U.S. FDA** and **China NMPA** regulatory frameworks.

The dataset is designed to assess not only monolingual regulatory retrieval, but also **explicit cross-jurisdictional comparison**, a setting that requires concept-level alignment across non-equivalent administrative and legal systems.

---

## Quick Facts

- **Domain**: Pharmaceutical regulation (FDA vs NMPA)
- **Task Format**: Multiple-choice question answering (MCQA)
- **Task Types**: Monolingual · Comparative · Parallel
- **Languages**: English / Chinese
- **Size**: 11,871 questions
- **License**: CC BY 4.0
- **Paper**: *Sino-US-DrugQA: A Benchmark for Evaluating Large Language Models in Cross-Jurisdictional Pharmaceutical Regulation*

---

## Dataset Overview

### Key Statistics

- **Total QA pairs**: 11,871
- **Task distribution**:
  - Monolingual QA: 7,013 (59.1%)
  - Comparative QA: 4,310 (36.3%)
  - Parallel QA: 548 (4.6%)
- **Language distribution**:
  - English: 6,069 (51.1%)
  - Chinese: 5,802 (48.9%)

### Regulatory Domain Coverage (Top 5)

- Drugs: 4,752 (40.0%)
- Medical Devices: 2,772 (23.4%)
- Cosmetics: 1,699 (14.3%)
- General FDA: 1,465 (12.3%)
- Controlled Substances: 845 (7.1%)

---

## Task Definitions

- **Monolingual QA**  
  Retrieval and interpretation of regulatory requirements within a single jurisdiction (FDA *or* NMPA).

- **Comparative QA**  
  Explicit comparison of regulatory requirements across jurisdictions (e.g., timelines, thresholds, procedural obligations).

- **Parallel QA**  
  Structurally aligned questions asked independently in English and Chinese to assess bilingual consistency.

---

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

---

## Data Format

Each instance is stored as one line in a JSONL file:

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

### Field Definitions

- `id`: unique question identifier
- `question`: question text
- `choices`: four answer options (A-D)
- `answer`: correct option label
- `type`: one of `{Monolingual, Comparative, Parallel}`
- `category`: regulatory domain
- `lang`: one of `{EN, CN}`
- `explanation`: rationale grounded in regulatory text
- `source_cn` / `source_us`: regulatory source references (when applicable)

See `DATASET_CARD.md` for full details.

---

## Data Splits

- `data/0-shot/`  
  Full dataset and type-specific JSONL files used for zero-shot evaluation.

- `data/5-shot/`  
  Dev/test splits for few-shot evaluation (5 examples per task type in dev).

---

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

---

## Evaluation

Run baseline evaluations using the provided scripts:

```bash
./scripts/run_deepseek.sh
./scripts/run_gpt.sh
./scripts/run_gemini.sh
./scripts/run_qwen.sh
```

Few-shot evaluation can be enabled via:

```bash
SHOT=5 ./scripts/run_deepseek.sh
```

Models evaluated in the accompanying paper:

- DeepSeek-V3.2
- GPT-5.2
- Qwen-3-235B
- Gemini-3-flash

---

## Intended Use

Sino-US-DrugQA is intended for **research and benchmarking** of LLMs in regulatory intelligence, particularly for evaluating:

- Cross-jurisdictional regulatory reasoning
- Bilingual regulatory comprehension (EN/ZH)
- Concept-level alignment across non-isomorphic legal systems
- Regulatory hallucination and misalignment errors

Outputs should **not** be used as standalone regulatory advice.
All real-world compliance decisions must remain subject to expert review.

---

## Source Documents

Original regulatory texts are publicly available from official portals:

- NMPA: https://www.nmpa.gov.cn
- US FDA (eCFR Title 21): https://www.ecfr.gov

To respect source authority and ensure regulatory currency, original regulatory documents are **not redistributed** in this repository.

---

## License

This dataset is released under the **Creative Commons Attribution 4.0 (CC BY 4.0)** license.
See `LICENSE` for details.

---

## Citation

If you use Sino-US-DrugQA in your research, please cite the accompanying paper:

See `CITATION.bib`.
