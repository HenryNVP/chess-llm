import pandas as pd
from collections import Counter

# Load the CSV file
def load_data(file_path):
    """Loads the chess puzzle data from a CSV file."""
    return pd.read_csv(file_path)

# Perform Exploratory Data Analysis
def eda(df):
    """Performs Exploratory Data Analysis on the dataframe."""
    print("\n=== EDA ===\n")
    
    # 1. Shape of the dataframe
    print(f"Shape of the dataframe: {df.shape}\n")
    
    # 4. Summary statistics for numerical columns
    print("Summary statistics for numerical columns:")
    print(df.describe())
    print("\n")
    

# Split the 'Themes' column into a list of individual themes
def split_themes(df):
    """Splits the 'Themes' column into a list of individual themes."""
    df['Themes_split'] = df['Themes'].str.split()
    return df

# Filter the dataframe for rows containing a specific theme
def filter_by_theme(df, target_theme):
    """Filters the dataframe for rows that contain a specific theme."""
    filtered_df = df[df['Themes_split'].apply(lambda x: target_theme in x if isinstance(x, list) else False)]
    return filtered_df

# Count the occurrences of each theme
def count_themes(df):
    """Counts the occurrences of each theme in the dataframe."""
    theme_counter = Counter([theme for sublist in df['Themes_split'].dropna() for theme in sublist])
    print("Theme counts:\n", theme_counter)
    return theme_counter


# Main function to load data, perform EDA, and filter by theme
def main(file_path, target_theme):
    """Main function that loads data, performs EDA, splits themes, and filters by a target theme."""
    # Load data
    df = load_data(file_path)
    
    # Perform EDA
    eda(df)
    
    # Split themes
    df = split_themes(df)
    
    # Filter rows containing the target theme
    filtered_df = filter_by_theme(df, target_theme)
    print(f"\nNumber of puzzles with the theme '{target_theme}': {filtered_df.shape[0]}")
    print(filtered_df.head())
    
    # Save the filtered data to a CSV file
    filtered_df.to_csv(f'filtered_puzzles_{target_theme}.csv', index=False)
    print(f"\nFiltered puzzles with the theme '{target_theme}' saved to 'filtered_puzzles_{target_theme}.csv'\n")
    
    # Count theme occurrences
    count_themes(df)
    
# Run the script with the desired file path and target theme
if __name__ == "__main__":
    file_path = 'puzzles_db.csv'  # Replace with your file path
    target_theme = 'fork'  # Replace with the theme you're filtering for
    main(file_path, target_theme)
