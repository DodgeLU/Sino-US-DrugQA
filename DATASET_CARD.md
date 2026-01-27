# Dataset Card: Sino-US-DrugQA

## Summary

Sino-US-DrugQA is a bilingual benchmark for evaluating large language models on
cross-jurisdictional pharmaceutical regulation. The dataset focuses on US FDA
and China NMPA regulations and targets both monolingual retrieval and explicit
cross-jurisdictional comparison tasks.

## Languages

- English (EN)
- Chinese (ZH)

## Task Types

- Monolingual QA: retrieve facts within one jurisdiction.
- Comparative QA: compare requirements across US vs China.
- Parallel QA: aligned questions in both languages for consistency checks.

## Size and Splits

- Total: 11,871 QA pairs
- Monolingual: 7,013 (59.1%)
- Comparative: 4,310 (36.3%)
- Parallel: 548 (4.6%)
- English: 6,069 (51.1%)
- Chinese: 5,802 (48.9%)

Splits used in this repo:

- `data/0-shot/`: full dataset and type-specific JSONL files
- `data/5-shot/`: dev/test split per type (5 examples per type in dev)

## Fields

- `id`: unique question identifier
- `question`: question text
- `choices`: 4 options (A/B/C/D)
- `answer`: correct option label (A/B/C/D)
- `type`: Monolingual | Comparative | Parallel
- `category`: regulatory domain (e.g., Drugs, Medical_Devices, GMP)
- `lang`: EN | CN
- `explanation`: rationale for the answer
- `source_cn` / `source_us`: source document references (when applicable)

## Source Data

- 134 key NMPA regulations
- 195 documents from US CFR Title 21

## Domain Coverage (Top 5)

- Drugs: 4,752 (40.0%)
- Medical Devices: 2,772 (23.4%)
- Cosmetics: 1,699 (14.3%)
- General_FDA: 1,465 (12.3%)
- Controlled Substances: 845 (7.1%)

Original regulations are publicly available from official portals:

- https://www.nmpa.gov.cn
- https://www.ecfr.gov

## Intended Use

Research and benchmarking of LLMs for regulatory intelligence, with emphasis
on cross-jurisdictional comparison. Outputs should be reviewed by experts for
any real-world compliance use.

## License

CC BY 4.0
