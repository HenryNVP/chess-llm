import pandas as pd
import chess

def apply_first_move(fen, moves):
    """
    Applies the first move to the given FEN string and removes it from the moves.
    Applicable for Lichess puzzles database
    """
    # Create a chess board from the FEN string
    board = chess.Board(fen)
    
    # Extract the first move and the remaining moves
    move_list = moves.split()
    first_move = move_list[0]
    remaining_moves = " ".join(move_list[1:])
    
    # Apply the first move
    board.push_san(first_move)
    
    # Get the new FEN after the first move
    new_fen = board.fen()
    
    return new_fen, remaining_moves

def process_puzzle_data(file_path, output_file_path):
    df = pd.read_csv(file_path)
    
    # Apply the first move to all FENs and modify the Moves column
    df['Updated_FEN'], df['Updated_Moves'] = zip(*df.apply(lambda row: apply_first_move(row['FEN'], row['Moves']), axis=1))
    
    # Save the updated dataframe to a new CSV file
    df.to_csv(output_file_path, index=False)
    print(f"Updated puzzles saved to {output_file_path}")

file_path = 'puzzles_db.csv'
output_file_path = 'updated_puzzles.csv'

# Process the puzzle data
process_puzzle_data(file_path, output_file_path)
