# Sino-US-DrugQA

**Sino-US-DrugQA** 是一个中英双语基准数据集，用于评估大语言模型在
**跨法域药品监管推理**中的能力，重点关注 **US FDA** 与 **China NMPA**
监管体系的比较理解与对齐。

与传统法律或医学基准不同，Sino-US-DrugQA 聚焦 **行政监管合规任务**，
要求模型在 **非等价监管体系**中进行对齐、比较与推断。

---

## 🔍 本基准评测什么

Sino-US-DrugQA 用于评估模型是否能够：

- 在单一法域内检索监管要求
- 跨法域进行比较（如时限、阈值、流程义务）
- 保持概念级别对齐（FDA vs. NMPA）
- 避免幻觉或过度泛化的合规结论

该基准仅用于**评测与研究**，不用于自动化合规决策。

---

## 📊 数据集概览

- **总题量**：11,871 道多选题
- **语言**：英文 51.1%，中文 48.9%
- **法域**：US FDA（CFR Title 21）与中国 NMPA
- **任务类型**：
  - Monolingual：59.1%
  - Comparative：36.3%
  - Parallel：4.6%
- **来源文档**：
  - 134 部 NMPA 法规
  - 195 份 CFR Title 21 文档

---

## 🧠 任务类型

| 类型 | 描述 |
| --- | --- |
| Monolingual | 单一法域内的监管检索 |
| Comparative | 明确要求跨法域比较 |
| Parallel | 以等价问题测试一致性 |

---

## 🏷 监管领域（Top 5）

| 领域 | 占比 |
| --- | --- |
| Drugs | 40.0% |
| Medical Devices | 23.4% |
| Cosmetics | 14.3% |
| General FDA / Administrative | 12.3% |
| Controlled Substances | 7.1% |

---

## 🤖 Zero-shot 基线模型（总体准确率）

| 模型 | 准确率 |
| --- | --- |
| Gemini-3-flash | 84.51% |
| DeepSeek-V3.2 | 80.53% |
| Qwen-3-235B | 80.04% |
| GPT-5.2 | 78.97% |

所有评测均使用**统一 Zero-shot 与 Five-shot 协议**，温度设置为 0。

---

## 📁 仓库结构

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

## 🧾 数据格式

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

完整字段说明见 `DATASET_CARD.md`。

---

## 📦 数据划分

- `data/0-shot/`：全量数据与按类型拆分后的 JSONL
- `data/5-shot/`：按类型划分 dev/test（每类 dev 取 5 条）

---

## 📌 提示词模板（Zero-shot）

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

## 🧪 评测

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

模型名称与论文保持一致：

- DeepSeek-V3.2
- GPT-5.2
- Qwen-3-235B
- Gemini-3-flash

---

## 📜 数据来源

原始法规来自公开官方渠道：

- NMPA: https://www.nmpa.gov.cn
- eCFR Title 21: https://www.ecfr.gov

---

## ⚠️ 使用范围与免责声明

本数据集用于：

- 监管推理基准评测
- 跨法域对齐研究
- 误差分析与鲁棒性研究

不用于：

- 自动化合规决策
- 无专家审查的法律或合规建议

---

## 📄 许可协议

本数据集采用 CC BY 4.0 协议，详见 `LICENSE`。

---

## 📚 引用

见 `CITATION.bib`。
