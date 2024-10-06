import streamlit as st
import chess
import chess.engine
from tactic_generation import generate_fen
from stockfish_engine import validate_fen
from feedback_storage import store_feedback

# Chess engine (Stockfish)
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

# Streamlit UI
st.title("Chess Tactic Generator")

# Generate a new FEN code and move
fen, move = generate_fen()
board = chess.Board(fen)

st.write(f"Generated FEN: `{fen}`")
st.write(f"Suggested Move: `{move}`")

# Display the chessboard
st_chessboard = st.empty()
st_chessboard.text(board)

# Feedback input (correct or incorrect)
st.write("Is this position correct?")
feedback = st.radio("Feedback", ("Correct", "Incorrect"))

if feedback == "Incorrect":
    correct_fen = st.text_input("Enter the correct FEN:")
    correct_move = st.text_input("Enter the correct move:")
    
    # Store the feedback for future retraining
    store_feedback(fen, move, correct_fen, correct_move)
    st.write("Feedback stored!")

# Validate with Stockfish
if st.button("Validate with Stockfish"):
    is_valid = validate_fen(fen, move)
    if is_valid:
        st.write("The generated move is correct!")
    else:
        st.write("The generated move is incorrect!")
