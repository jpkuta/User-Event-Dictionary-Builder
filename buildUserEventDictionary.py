import json

# Read input JSON file
with open('input.json', 'r') as f:
    data = json.load(f)

# Create dictionary to aggregate timestamp data
aggregated_timestamp_data = {}
# Create dictionary to aggregate command frequency data
aggregated_freq_data = {}

# Iterate over events and aggregate timestamp data for user events
for event in data:
    user = event['user']
    command = event['command']
    timestamp = event['timestamp']
    
    if user not in aggregated_timestamp_data:
        aggregated_timestamp_data[user] = {}
    if command not in aggregated_timestamp_data[user]:
        aggregated_timestamp_data[user][command] = []
    
    aggregated_timestamp_data[user][command].append(timestamp)

# Iterate over events and aggregate frequency data
for event in data:
    user = event['user']
    command = event['command']
    
    if user not in aggregated_freq_data:
        aggregated_freq_data[user] = {}
    
    if command not in aggregated_freq_data[user]:
        aggregated_freq_data[user][command] = 1
    else:
        aggregated_freq_data[user][command] += 1

# Write aggregated timestamp data to output.json file
with open('output.json', 'w') as f:
    json.dump(aggregated_timestamp_data, f, indent=4)

# Write aggregated frequency data to output JSON file
with open('frequency_output.json', 'w') as f:
    json.dump(aggregated_freq_data, f, indent=4)