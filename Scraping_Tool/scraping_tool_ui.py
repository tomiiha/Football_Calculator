import ipywidgets as widgets

# Capture files for processing
def initial_load():
    import os
    import json
    data_filename = [data_file for data_file in os.listdir() 
                 if data_file.endswith('.json')]
    with open(data_filename[0]) as json_file:
            data = json.load(json_file)
    return league_select(data)

# Pick league.
def league_select(data):
    league_list = []
    for y in data:
        if y['Competition'] is not None and y['Competition'] not in league_list:
            league_list.append(y['Competition'])
    return team_list_create(league_list, data)

# Pull league teams per selection
def team_list_create(league_list, data):
    league_choice = league_list[1]
    team_list = []
    for x in data:
        if x['Competition'] == league_choice:
            team_list.append(x['Team'])
    return team_picker(team_list)

# UI content
def ui_content(league_list):
    league_box=Dropdown(
        options=league_list,
        value='Choose League',
        description='Select Sector:',
        layout={'width': 'max-content'},
        style = {'description_width': 'initial'},
        disabled=False,
    )
    return ui_final(league_box):
    
# UI Execution    
def ui_final(league_box):
    ui = VBox(layout=Layout(width='2000px',margin = ' 20px 0 0 20px '))
    ui.children = [sector_box, snapshot_time_box, machine_box, snapshot_date, run_button, status_label, out]
    return display(ui)
