from transformers import AutoTokenizer, AutoModelForCausalLM

# Load your fine-tuned chess tactic model here
tokenizer = AutoTokenizer.from_pretrained("your-fine-tuned-model")
model = AutoModelForCausalLM.from_pretrained("your-fine-tuned-model")

def generate_tactic(tactic_type="fork"):
    # Placeholder generation logic
    input_text = f"Generate {tactic_type} tactic"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
