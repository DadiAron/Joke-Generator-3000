from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
# Skilgreinum slóðina að fínþjálfaða líkaninu okkar
model_path = "DadiAron/joke-generator-3000"

# Setjum tokenizer og model sem okkar líkan
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Setja líkanið í evaluation ham til þess að geta fengið betri úttök
model.eval()

# Setjum ákveðnar stillingar fyrir úttakið
def generate_joke(prompt: str) -> str:
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=128,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded[len(prompt):].strip()