import json

input_file = 'CORWA_test.jsonl' # switch to the file needed
output_file = 'test.json' # switch the name likewise

with open(input_file, 'r') as f:
    json_lines = [json.loads(line) for line in f]

with open(output_file, 'w') as f:
    json.dump(json_lines, f, indent=4)
