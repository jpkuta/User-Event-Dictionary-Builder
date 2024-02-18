# User-Event-Dictionary-Builder
## Description
This python script aggrigates user timestamp data from a input.json file. The results are in the output.json file. 
Additionally there is a method which outputs how many times each command was executed by a user. This aids in identifying the most frequent commands utilized by each user. Output found in the frequency_output.json file.
Finally there is a method which returns the 3 top active users with the number of commands which they ran. This data can be used to identify the most active users in the system.Output found in the top_3_active_users_output.json file.


## How to use
                
1. download script
2. place 'input.json' input file in the same directory as buildUserEventDictionary.py script
3. execute 'python buildUserEventDictionary.py'
4. See 'output.py', 'frequency_output.json' and 'top_3_active_users_output.json' output files in the excuted directory