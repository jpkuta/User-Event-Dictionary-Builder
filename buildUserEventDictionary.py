import json
from collections import defaultdict

# Read input JSON file
with open('input.json', 'r') as f:
    data = json.load(f)

# Create dictionaries to aggregate data
aggregated_timestamp_data = defaultdict(lambda: defaultdict(list))
aggregated_freq_data = defaultdict(lambda: defaultdict(int))
user_activity = defaultdict(int)

# Iterate over events and aggregate data
for event in data:
    user = event['user']
    command = event['command']
    timestamp = event['timestamp']
    
    # Aggregate timestamp data
    aggregated_timestamp_data[user][command].append(timestamp)
    
    # Aggregate frequency data
    aggregated_freq_data[user][command] += 1
    
    # Aggregate user activity data
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
