import pandas as pd
from collections import Counter


def filter_by_theme(df, target_theme):
    # Filters the dataframe for rows where the 'Themes' column contains the target theme
    filtered_df = df[df['Themes'].str.contains(
        target_theme, case=False, na=False)]
    return filtered_df


if __name__ == "__main__":
    file_path = 'puzzles_db.csv'
    df = pd.read_csv(file_path)

    # Filter rows containing the target theme
    target_theme = 'mateIn2'
    filtered_df = filter_by_theme(df, target_theme)
    print(
        f"\nNumber of puzzles with the theme '{target_theme}': {filtered_df.shape[0]}")
    pd.set_option('display.max_columns', None)
    print(filtered_df.head())

    # Save the filtered data to a CSV file
    filtered_df.to_csv(f'puzzles_{target_theme}.csv', index=False)
    print(
        f"\nFiltered puzzles with the theme '{target_theme}' saved to 'puzzles_{target_theme}.csv'\n")
