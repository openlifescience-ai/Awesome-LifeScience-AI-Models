import json

# Load metadata.json
with open('metadata.json', 'r') as f:
    data = json.load(f)

# Generate table
table = "| Name | Source |\n| --- | --- |\n"
for item in data:
    name = item['name']
    source_name = item['source']['name']
    source_url = item['source']['url']
    table += f"| {name} | [{source_name}]({source_url}) |\n"

# Write to README.md
with open('README.md', 'w') as f:
    f.write(table)
