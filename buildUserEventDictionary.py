import json

# Read input JSON file
with open('input.json', 'r') as f:
    data = json.load(f)

# Create dictionary to aggregate timestamp data
aggregated_timestamp_data = {}
# Create dictionary to aggregate command frequency data
aggregated_freq_data = {}
# Create dictionary to aggregate user activity data
user_activity = {}

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

# Iterate over events and aggregate user activity data
for event in data:
    user = event['user']
    
    if user not in user_activity:
        user_activity[user] = 1
    else:
        user_activity[user] += 1

# Sort the users based on activity
sorted_users = sorted(user_activity.items(), key=lambda x: x[1], reverse=True)

# Get the top 3 most active users
top_users = sorted_users[:3]

# Write aggregated timestamp data to output.json file
with open('output.json', 'w') as f:
    json.dump(aggregated_timestamp_data, f, indent=4)

# Write aggregated frequency data to frequency_output.json file
with open('frequency_output.json', 'w') as f:
    json.dump(aggregated_freq_data, f, indent=4)

# Write top users to output top_3_active_users_output.json file
with open('top_3_active_users_output.json', 'w') as f:
    json.dump(top_users, f, indent=4)