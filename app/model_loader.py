from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_path = "DadiAron/joke-generator-3000"

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
model.eval()

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