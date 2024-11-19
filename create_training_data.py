import pandas as pd
import json  # Import the json module to handle proper formatting

def create_training_data(df, target_theme):
    # Filter rows based on the target theme
    df = df[df['Themes'].str.contains(target_theme, case=False, na=False)]
    
    # Generate the training data for the specified theme
    training_data = []
    for _, row in df.iterrows():
        input_data = f"Create a chess puzzle with theme {target_theme}"
        output_data = f"FEN: {row['FEN']} Moves: {row['Moves']}"
        training_data.append({"input": input_data, "output": output_data})
    
    return training_data

if __name__ == "__main__":
    file_path = 'puzzles_db.csv'
    df = pd.read_csv(file_path)
    
    target_theme = 'mateIn2'
    
    # Generate the training data
    training_data = create_training_data(df, target_theme)
    
    output_file = f'puzzles_{target_theme}.jsonl'
    with open(output_file, 'w') as f:
        for entry in training_data:
            json.dump(entry, f)
            f.write("\n")  # Write each JSON object on a new line
    
    print(f"\nTraining data for theme '{target_theme}' saved to '{output_file}'")
