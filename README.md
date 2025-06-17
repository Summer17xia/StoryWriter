# StoryWriter

**StoryWriter** is a multi-agent framework for generating high-quality **long stories** with logical coherence and engaging plots—two major challenges that remain unsolved for most current large language models (LLMs).

---

## ✨ Highlights

Long story generation is hard due to:

1. **Discourse Coherence**
   Maintaining consistency, logic, and completeness throughout the story.

2. **Narrative Complexity**
   Crafting engaging, interwoven plots across characters and events.

To tackle these, we introduce **`StoryWriter`**, a **multi-agent story generation framework** with the following components:

* **🧠 Outline Agent**
  Produces event-based outlines rich in plots, characters, and inter-event relationships.

* **🗂️ Planning Agent**
  Breaks down the outline into chapter-wise plans, ensuring an engaging, interwoven narrative.

* **✍️ Writing Agent**
  Dynamically compresses the story history to generate coherent new content aligned with the current event.

---

## 📊 Results

We conduct both human and automatic evaluations, and **StoryWriter** significantly **outperforms** existing baselines in:

以下是将你提供的 LaTeX 表格 **转化成 Markdown 表格** 的版本，适合放在 README 或 Markdown 文档中使用（注意 Markdown 表格不支持复杂合并、换行和自动缩放，但可以用简洁清晰的方式呈现核心内容）：

---

### 📊 Experimental Results (%) of StoryWriter Variants and Baselines

> * `S_q`: Average quality score over 6 dimensions
> * `S_l`: Length score (see Equation\~\ref{eq\:eq\_sl})
> * `S̄`: Final score, computed as `(S_q + 20 × S_l) / 2`
> * **Bold** indicates the best result in each column
| Model                      | **S̄**   | S\_l     | S\_q    | \[0,1k) S\_l | S\_q    | \[1k,2k) S\_l | S\_q    | \[2k,4k) S\_l | S\_q    | \[4k,10k) S\_l | S\_q    | \[10k,20k) S\_l | S\_q    |
| -------------------------- | -------- | -------- | ------- | ------------ | ------- | ------------- | ------- | ------------- | ------- | -------------- | ------- | --------------- | ------- |
| **Llama3.1-8B-Instruct**   | 46.6     | 34.5     | 2.9     | 89.0         | 4.0     | 83.7          | 3.9     | 0.0           | 3.5     | 0.0            | 2.2     | 0.0             | 1.0     |
| **GLM4-9B**                | 47.3     | 36.6     | 2.9     | 93.7         | 4.2     | 89.6          | 4.0     | 0.0           | 3.3     | 0.0            | 2.0     | 0.0             | 1.0     |
| **LongWriter-GLM4-9B**     | 76.3     | 83.0     | 3.5     | 86.9         | 3.1     | 93.1          | 3.2     | 91.6          | 4.0     | 86.9           | 3.6     | 56.7            | 3.4     |
| **LongWriter-Llama3.1-8B** | 77.9     | 83.6     | 3.6     | 96.9         | 3.9     | 96.1          | 3.5     | 93.2          | 4.1     | 81.9           | 3.5     | 51.3            | 3.2     |
| **Deepseek-Llama-8B**      | 70.0     | 73.6     | 3.3     | 92.3         | 3.1     | 91.9          | 3.2     | 88.2          | 3.6     | 83.2           | 3.4     | 12.3            | 3.3     |
| **Deepseek-Llama-70B**     | 74.3     | 79.0     | 3.5     | 93.2         | 3.3     | 94.5          | 3.4     | 87.2          | 4.0     | 81.0           | 3.5     | 44.1            | 3.2     |
| **GPT-4o**                 | 67.4     | 52.8     | **4.1** | 92.3         | **4.7** | 91.7          | **4.5** | 62.0          | **4.3** | 15.3           | **3.7** | 2.7             | 3.3     |
| **StoryWriter-LLaMA**      | 73.4     | 75.3     | 3.5     | 90.8         | 3.9     | 94.1          | 3.8     | 77.3          | 3.5     | 77.0           | 3.4     | 27.7            | 3.4     |
| **StoryWriter-GLM**        | **83.7** | **88.5** | 3.9     | **99.5**     | 4.4     | **99.3**      | 4.1     | **98.0**      | 4.0     | **88.7**       | 3.5     | **57.3**        | **3.6** |


---

如你需要更好看的交互式表格效果，建议：

* 用 HTML 表格嵌入 Markdown
* 或在网页中使用 JS 表格库（如 DataTables）

如需我进一步生成 HTML 版本或插入图表、强调趋势，也可以继续告诉我。


---

## 📚 Dataset

We use StoryWriter to generate a large-scale long story dataset:

* **\~6,000 stories**
* **Average length: 8,000 words/story**

---

## 🔧 Model Training

Using this dataset, we fine-tuned:

* **`LLaMA3.1-8B` → `StoryWriter-LLaMA`**
* **`GLM4-9B` → `StoryWriter-GLM`**

These models exhibit strong performance in long-form story generation.

---

## 📥 Get Started

* **📖 Read Sample Stories**
  Download generated stories here:
  👉 [Tsinghua Cloud Link](https://cloud.tsinghua.edu.cn/f/6173850b58114951ab7e/)

* **🛠️ Train Your Own Model**
  Use [LongWriter](https://github.com/THUDM/LongWriter/tree/main) to train on our dataset.
  Replace the original raw file with our training JSON.
