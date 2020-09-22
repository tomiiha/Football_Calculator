# Capture files for processing
def initial_load():
    import os
    import json
    data_filename = [data_file for data_file in os.listdir() 
                 if data_file.endswith('.json')]
    with open(data_filename[0]) as json_file:
            data = json.load(json_file)
    return league_picker(data)

# Pick league.
def league_picker(data):
    league_choice = 'EFL League One'
    team_list = []
    for x in data:
        if x['Competition'] == league_choice:
            team_list.append(x['Team'])
    return team_picker(team_list)
    
# Pick team
def team_picker(team_list):
    print(team_list)
    return
    
initial_load()
