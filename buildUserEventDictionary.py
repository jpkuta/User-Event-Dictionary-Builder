import json

# Read input JSON file
with open('input.json', 'r') as f:
    data = json.load(f)

# Create dictionary to aggregate data
aggregated_data = {}

# Iterate over events and aggregate data
for event in data:
    user = event['user']
    command = event['command']
    timestamp = event['timestamp']
    
    if user not in aggregated_data:
        aggregated_data[user] = {}
    if command not in aggregated_data[user]:
        aggregated_data[user][command] = []
    
    aggregated_data[user][command].append(timestamp)

# Write aggregated data to output JSON file, save output to same directory as this script
with open('output.json', 'w') as f:
    json.dump(aggregated_data, f, indent=4)
