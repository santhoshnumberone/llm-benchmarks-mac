# benchmark_llamacpp.py
from llama_cpp import Llama
from pathlib import Path
import time

models = [
    "mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    "zephyr-7b-beta.Q4_K_M.gguf"
]

for model_file in models:
    print(f"🧠 Model: {model_file}")
    model_path = (Path(__file__).parent / "shared/models" / model_file).resolve() # change the path here

    start = time.time()
    llm = Llama(
        model_path=str(model_path),
        n_ctx=512,
        n_threads=4,
        verbose=False
    )
    output = llm("Can I sublicense an open source license?", max_tokens=64)
    end = time.time()

    print(f"📤 Output: {output['choices'][0]['text'].strip()}")
    print(f"⏱️ Time taken: {end - start:.4f} seconds\n")
