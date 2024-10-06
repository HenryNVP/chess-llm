def store_feedback(incorrect_fen, incorrect_move, correct_fen, correct_move):
    # Save the feedback in a file for future retraining
    with open("corrected_data.txt", "a") as f:
        f.write(f"Incorrect FEN: {incorrect_fen}, Move: {incorrect_move}\n")
        f.write(f"Correct FEN: {correct_fen}, Move: {correct_move}\n")
