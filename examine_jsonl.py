import json

# Initialize a counter for the number of valid rows
valid_rows = 0
invalid_rows = 0

# List to store the first 10000 examples
first_10000_examples = []

# Open the file to check its format
with open("puzzles_mateIn2.jsonl", "r") as f:
    for i, line in enumerate(f):
        try:
            json_data = json.loads(line.strip())
            valid_rows += 1
            
            # Add the first 10000 examples to the list
            if len(first_10000_examples) < 10000:
                first_10000_examples.append(json_data)
        
        except json.JSONDecodeError as e:
            invalid_rows += 1
            print(f"Error on line {i+1}: {e}")

print(f"Number of valid rows: {valid_rows}")
print(f"Number of invalid rows: {invalid_rows}")

# Save the first 10000 examples to a new JSONL file
output_file = "puzzles_mateIn2_10000.jsonl"
with open(output_file, "w") as outfile:
    for example in first_10000_examples:
        json.dump(example, outfile)
        outfile.write("\n")

print(f"First 10000 examples saved to '{output_file}'")
