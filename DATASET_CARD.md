# Dataset Card: Sino-US-DrugQA

## Dataset Summary

Sino-US-DrugQA is a bilingual benchmark dataset designed to evaluate the ability of large language models (LLMs) to perform **cross-jurisdictional pharmaceutical regulatory reasoning**. The dataset focuses on regulatory frameworks administered by the **United States Food and Drug Administration (FDA)** and **China’s National Medical Products Administration (NMPA)**.

Unlike existing legal or medical benchmarks that primarily target monolingual statutory interpretation or clinical decision-making, Sino-US-DrugQA emphasizes **administrative regulatory compliance** and **explicit comparison across non-equivalent legal systems**, such as differences in procedural timelines, approval requirements, and documentation obligations.

The dataset is intended for **evaluation and benchmarking purposes only** and does not constitute legal or regulatory advice.

---

## Languages

- English (EN)
- Chinese (ZH)

---

## Task Types

Sino-US-DrugQA includes three task types reflecting different regulatory reasoning demands:

- **Monolingual QA**  
  Retrieval and interpretation of regulatory requirements within a single jurisdiction (FDA or NMPA).

- **Comparative QA**  
  Explicit comparison of regulatory requirements across jurisdictions, requiring concept-level alignment (e.g., identifying which jurisdiction has stricter timelines or additional procedural steps).

- **Parallel QA**  
  Aligned questions asked separately for FDA and NMPA to evaluate cross-lingual and cross-jurisdictional consistency.

---

## Dataset Size and Composition

- **Total QA pairs**: 11,871

### Task Distribution

- Monolingual QA: 7,013 (59.1%)
- Comparative QA: 4,310 (36.3%)
- Parallel QA: 548 (4.6%)

### Language Distribution

- English: 6,069 (51.1%)
- Chinese: 5,802 (48.9%)

---

## Data Splits

The repository provides evaluation-oriented splits:

- `data/0-shot/`  
  Full dataset and task-type–specific JSONL files for zero-shot evaluation.

- `data/5-shot/`  
  Development and test splits per task type, where the development set contains **5 examples per task type**, used exclusively for in-context learning in few-shot evaluation.

No training split is provided, as the dataset is designed for **benchmarking rather than model training**.

---

## Data Fields

Each instance is stored as a single JSON object with the following fields:

- `id`: Unique question identifier
- `question`: Question text
- `choices`: List of four answer options (A/B/C/D)
- `answer`: Correct option label (A/B/C/D)
- `type`: Task type (`Monolingual`, `Comparative`, or `Parallel`)
- `category`: Regulatory domain (e.g., `Drugs`, `Medical_Devices`, `GMP`)
- `lang`: Language of the question (`EN` or `CN`)
- `explanation`: Brief rationale for the correct answer (not used for scoring)
- `source_cn`: Reference to the originating NMPA regulatory provision (when applicable)
- `source_us`: Reference to the originating US CFR provision (when applicable)

The `source_cn` and `source_us` fields enable **traceability** to authoritative regulatory texts.

---

## Source Data

The dataset was constructed from publicly available regulatory documents, including:

- **134 key NMPA regulations**
- **195 documents from the US Code of Federal Regulations (CFR), Title 21**

Original regulatory texts are available from official sources:

- NMPA: https://www.nmpa.gov.cn  
- US eCFR (Title 21): https://www.ecfr.gov  

The dataset reflects regulatory versions effective as of **December 2025**.

---

## Domain Coverage (Top 5)

- Drugs: 4,752 (40.0%)
- Medical Devices: 2,772 (23.4%)
- Cosmetics: 1,699 (14.3%)
- General FDA / Administrative: 1,465 (12.3%)
- Controlled Substances: 845 (7.1%)

---

## Intended Use

This dataset is intended for:

- Benchmarking LLM performance on pharmaceutical regulatory reasoning
- Research on cross-jurisdictional AI alignment and robustness
- Error analysis in high-stakes regulatory question answering

Any outputs generated using this dataset **must be reviewed by qualified regulatory professionals** before being used in real-world compliance or decision-making contexts.

---

## Out-of-Scope Use

The dataset is **not intended** for:

- Automated regulatory decision-making
- Legal or compliance advice without expert oversight
- Training production-grade regulatory AI systems without additional validation

---

## License

Sino-US-DrugQA is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
