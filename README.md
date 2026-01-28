# Sino-US-DrugQA

**Sino-US-DrugQA** 是一个中英双语基准数据集，用于评估大语言模型在
**跨法域药品监管推理**中的能力，重点关注 **U.S. FDA** 与 **China NMPA**
监管体系的比较理解与对齐。

本数据集不仅评估单一法域的监管检索能力，还覆盖**明确的跨法域比较**
场景，要求模型在非等价监管体系之间进行概念级别对齐与推理。

---

## Quick Facts

- **领域**：药品监管（FDA vs NMPA）
- **任务形式**：多项选择题（MCQA）
- **任务类型**：Monolingual · Comparative · Parallel
- **语言**：English / Chinese
- **规模**：11,871 题
- **许可证**：CC BY 4.0
- **论文**：*Sino-US-DrugQA: A Benchmark for Evaluating Large Language Models in Cross-Jurisdictional Pharmaceutical Regulation*

---

## 数据集概览

### 关键统计

- **总题量**：11,871
- **任务分布**：
  - Monolingual QA：7,013（59.1%）
  - Comparative QA：4,310（36.3%）
  - Parallel QA：548（4.6%）
- **语言分布**：
  - English：6,069（51.1%）
  - Chinese：5,802（48.9%）

### 监管领域分布（Top 5）

- Drugs：4,752（40.0%）
- Medical Devices：2,772（23.4%）
- Cosmetics：1,699（14.3%）
- General FDA：1,465（12.3%）
- Controlled Substances：845（7.1%）

---

## 任务定义

- **Monolingual QA**  
  单一法域内的监管检索与理解（FDA 或 NMPA）。

- **Comparative QA**  
  跨法域显式比较（如时限、阈值、流程义务）。

- **Parallel QA**  
  中英文结构对齐问题，用于一致性评测。

---

## 仓库结构

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

## 数据格式

`data/*.jsonl` 每行对应一个样本：

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

### 字段定义

- `id`：唯一题目编号
- `question`：题干
- `choices`：四个选项（A–D）
- `answer`：正确答案标签
- `type`：{Monolingual, Comparative, Parallel}
- `category`：监管领域
- `lang`：{EN, CN}
- `explanation`：依据法规文本的解释
- `source_cn` / `source_us`：来源法规（如适用）

完整字段说明见 `DATASET_CARD.md`。

---

## 数据划分

- `data/0-shot/`：全量数据与按类型拆分后的 JSONL
- `data/5-shot/`：按类型划分 dev/test（每类 dev 取 5 条）

---

## 提示词模板（Zero-shot）

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

## 评测

```bash
./scripts/run_deepseek.sh
./scripts/run_gpt.sh
./scripts/run_gemini.sh
./scripts/run_qwen.sh
```

脚本调用官方源站 API，并接受 `SHOT=0|5` 参数：

```bash
SHOT=5 ./scripts/run_deepseek.sh
```

论文中评测的模型：

- DeepSeek-V3.2
- GPT-5.2
- Qwen-3-235B
- Gemini-3-flash

---

## 使用范围

Sino-US-DrugQA 用于**监管智能评测与研究**，尤其包括：

- 跨法域监管推理
- 双语监管理解（EN/ZH）
- 非等价法域的概念对齐
- 幻觉与误配错误分析

⚠️ 输出**不应**用于自动化合规决策，任何真实合规结论必须由专家审查。

---

## 数据来源

原始法规来自公开官方渠道：

- NMPA: https://www.nmpa.gov.cn
- eCFR Title 21: https://www.ecfr.gov

---

为尊重原始法规权威性与时效性，原文法规不在本仓库重复发布。

---

## 许可协议

本数据集采用 CC BY 4.0 协议，详见 `LICENSE`。

---

## 引用

见 `CITATION.bib`。
