import csv

# Input and output file paths
input_file = 'lichess_db_puzzle.csv' 
output_file = 'puzzles_db.csv' 

# Columns we want to extract
columns_to_extract = ['FEN', 'Moves', 'Themes', 'Rating']

# Read the input CSV and write the extracted columns to the output CSV
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    # Open the output CSV for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)
        
        # Write header to the output CSV
        writer.writeheader()
        
        # Extract relevant columns and write each row to the new CSV
        for row in reader:
            writer.writerow({key: row[key] for key in columns_to_extract})

print(f"Extracted data saved to {output_file}")
