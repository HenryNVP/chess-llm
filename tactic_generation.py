from model import generate_tactic
import random

# Function to generate FEN and move using the fine-tuned model
def generate_fen():
    generated_tactic = generate_tactic("fork")
    # Assuming output is in the format "FEN move"
    fen, move = generated_tactic.split(' ')[0], generated_tactic.split(' ')[1]
    return fen, move
