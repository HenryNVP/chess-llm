import pandas as pd
from collections import Counter
import chess

def eda(df):
    # Perform Exploratory Data Analysis
    pd.set_option('display.max_columns', None)
    print(df.head())

    print(f"Shape of the dataframe: {df.shape}\n")

    # Summary statistics for numerical columns
    print("Summary statistics for numerical columns:")
    print(df.describe())
    print("\n")


def split_themes(df):
    # Split the 'Themes' column into a list of individual themes
    df['Themes_split'] = df['Themes'].str.split()
    return df


def count_themes(df):
    # Count the occurrences of each theme
    theme_counter = Counter(
        [theme for sublist in df['Themes_split'].dropna() for theme in sublist])
    print("Theme counts:\n", theme_counter)
    return theme_counter


def apply_first_move(fen, moves):
    """
    Applies the first move to the given FEN string and returns the new FEN and remaining moves.
    Uses the python-chess library to apply the move to the board.
    """
    # Create a chess board from the FEN string
    board = chess.Board(fen)
    
    # Extract the first move and the remaining moves
    move_list = moves.split()
    if len(move_list) > 0:
        first_move = move_list[0]  # First move (e.g., "e2e4")
        remaining_moves = " ".join(move_list[1:])  # The rest of the moves

        # Apply the first move
        try:
            board.push_san(first_move)
        except ValueError:
            print(f"Invalid move: {first_move}")
            return fen, moves  # Return the original FEN and moves if the move is invalid

        # Return the updated FEN and the remaining moves
        return board.fen(), remaining_moves
    
    return fen, moves  # Return unchanged if no moves exist


def apply_first_move_to_df(df):
    """
    Apply the first move to the FEN and modify the 'Moves' column directly in place.
    """
    # Apply the first move to the FEN and the remaining moves to the Moves column
    updated_fens_and_moves = df.apply(lambda row: apply_first_move(row['FEN'], row['Moves']), axis=1)
    
    # Unpack the results into two columns: 'FEN' and 'Moves'
    df['FEN'], df['Moves'] = zip(*updated_fens_and_moves)
    
    return df


def extract_data(df, output_file):
    # Save all themes, FEN, moves, and rating to a CSV file
    df[['Themes', 'FEN', 'Moves', 'Rating']].to_csv(output_file, index=False)
    print(f"Data saved to '{output_file}'")


if __name__ == "__main__":
    file_path = 'lichess_db_puzzle.csv'  # Path to your input CSV file
    df = pd.read_csv(file_path)

    # Perform EDA
    eda(df)
    
    df = df[['Themes', 'FEN', 'Moves', 'Rating']]

    # Split themes
    df = split_themes(df)

    # Count theme occurrences
    count_themes(df)

    # Apply the first move to the FEN and update the Moves column
    df = apply_first_move_to_df(df)

    # Save the updated data to a new CSV
    output_file = 'puzzles_db.csv'  # Output file path
    extract_data(df, output_file)
