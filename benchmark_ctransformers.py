# benchmark_ctransformers.py
from ctransformers import AutoModelForCausalLM
from pathlib import Path
import time

models = [
    ("mistral-7b-instruct-v0.1.Q4_K_M.gguf", "mistral"),
    ("zephyr-7b-beta.Q4_K_M.gguf", "mistral")
]

for model_file, model_type in models:
    print(f"🧠 Model: {model_file}")
    model_path = (Path(__file__).parent / "shared/models" / model_file).resolve() # Change path here
    
    start = time.time()
    model = AutoModelForCausalLM.from_pretrained(
        str(model_path),
        model_type=model_type,
        max_new_tokens=32,
        temperature=0.7
    )
    output = model("Can I sublicense an open source license?")
    end = time.time()

    print(f"📤 Output: {output.strip()}")
    print(f"⏱️ Time taken: {end - start:.4f} seconds\n")
