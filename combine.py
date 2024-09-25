import json

# Open the first file for reading
with open('autocomplete-nate.jsonl', 'r') as f1:
    # Read all lines from the file into a list
    data1 = [json.loads(line) for line in f1]

# Open the second file for reading
with open('autocomplete-patrick.jsonl', 'r') as f2:
    # Read all lines from the file into a list
    data2 = [json.loads(line) for line in f2]

# Combine the two lists of JSON objects
combined_data = data1 + data2

# Write the combined data to a new file
with open('combined.jsonl', 'w', encoding='utf8') as f:
    # Use json.dump() to write each JSON object on a separate line
    for obj in combined_data:
        data = json.dumps(obj, ensure_ascii=False)
        f.write(data)
        f.write('\n')
        