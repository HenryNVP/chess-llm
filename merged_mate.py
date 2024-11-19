import json

def merge_jsonl_files(file1, file2, output_file):
    with open(file1, 'r') as f1:
        data1 = [json.loads(line.strip()) for line in f1]
    
    with open(file2, 'r') as f2:
        data2 = [json.loads(line.strip()) for line in f2]
    
    merged_data = data1 + data2
    
    with open(output_file, 'w') as output:
        for entry in merged_data:
            json.dump(entry, output)
            output.write("\n")
    
    print(f"Files merged and saved to {output_file}")

file1 = 'puzzles_mateIn1_10000.jsonl'
file2 = 'puzzles_mateIn2_10000.jsonl'
output_file = 'puzzles_mateIn1_2_10000.jsonl'

merge_jsonl_files(file1, file2, output_file)
