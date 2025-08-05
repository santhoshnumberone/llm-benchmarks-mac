
# llm-benchmarks-mac

# 🧪 Benchmarking LLMs Locally on M1 MacBook Pro

A hands-on benchmark comparing `ctransformers` vs `llama.cpp` for local inference of quantized GGUF models (`mistral`, `zephyr`) on an M1 MacBook Pro (8GB RAM).

## 📊 Summary

| Library         | Speed        | Simplicity | Best Use Case                      |
|----------------|--------------|------------|------------------------------------|
| ctransformers   | ~15 seconds  | ✅ Easy     | Rapid prototyping                  |
| llama.cpp       | ~10 seconds  | ⚠️ Verbose  | RAG pipelines, speed-sensitive apps|

Follow the author on [LinkedIn](https://www.linkedin.com/in/santhosh-electraanu/)  

---

## 🛠 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/santhoshnumberone/llm-benchmarks-mac.git
cd llm-benchmarks-mac
```
### 2. Create and Activate a Python Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
`pip install -r requirements.txt`

### 4. Download Models

Download the `.gguf` files from Hugging Face, don't forget to change path inside code:

- [mistral-7b-instruct-v0.1.Q4_K_M.gguf](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
- [zephyr-7b-beta.Q4_K_M.gguf](https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF)

### ▶️ Run Benchmarks
ctransformers

`python benchmark_ctransformers.py`

llama.cpp via llama-cpp-python

`python benchmark_llamacpp.py`

### 📈 Example Output


| Model	| Library |	Time Taken |Output (Shortened)|
| ----- | ----- | ----- | ----- |
| Mistral |	ctransformers |	15.14s |"You may sublicense if terms are met..." |
| Zephyr |	llama-cpp-python |	12.63s |"It depends on the license..." |

### 🔍 Use Case
This repo is ideal for:
 - AI engineers testing local LLM inference
 - Prototyping RAG apps with speed constraints
 - Comparing backend performance tradeoffs

### 📬 Author
👤 Santhosh — Builder & AI Engineer

