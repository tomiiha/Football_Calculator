# Packaged used across functions - others in respective functions.
from bs4 import BeautifulSoup as bsoup
import requests as reqs
import json
import os
from ipywidgets import widgets, Dropdown, interact, interact_manual, Button, Output
from IPython.display import display

# Create team JSON file for parsing for front-end.
# the b variable here is just placed for the button interaction in UI.
def team_capture(b):
    # Purge old file(s).
    old_files = [data_file for data_file in os.listdir() 
                      if data_file.endswith('.json')]
    for old_json in old_files:
        os.remove(old_json)
    # Create new JSON file
    from datetime import date
    today = date.today().strftime('%Y%m%d')
    clubs_link = 'https://fbref.com/en/country/clubs/ENG/England-Football-Clubs'
    club_page = bsoup(reqs.get(clubs_link).content, 'html.parser')
    find_teams = club_page.find_all('tr')
    team_total = []
    file_name = 'team_list_' + str(today) + '.json'
    for x in find_teams[1:]:
        team_dict = {}
        add_team = x.find_next('th').get_text()
        team_dict['Team'] = add_team
        add_gen = x.find_next('td', attrs={"data-stat":"gender"}).get_text()
        team_dict['Gender'] = add_gen
        add_comp = x.find_next('td', attrs={"data-stat":"comp"}).get_text()
        team_dict['Competition'] = add_comp
        add_min = x.find_next('td', attrs={"data-stat":"min_season"}).get_text()
        team_dict['Earliest Season'] = add_min
        add_max = x.find_next('td', attrs={"data-stat":"max_season"}).get_text()
        team_dict['Latest Season'] = add_max
        add_total = x.find_next('td', attrs={"data-stat":"num_comps"}).get_text()
        team_dict['Total Seasons'] = add_total
        add_champs = x.find_next('td', attrs={"data-stat":"first_place_finishes"}).get_text()
        team_dict['Championships'] = add_champs
        add_names = x.find_next('td', attrs={"data-stat":"other_names"}).get_text()
        team_dict['Other Names'] = add_names
        # 'team_code' and 'team_prefix' for capturing season data later on.
        team_code = x.find_next('a').attrs['href']
        team_prefix = team_code[team_code.find('/history/') + 9:team_code.find('-and')]       
        team_code = team_code[11:team_code.find('/history/')]
        team_dict['Code'] = team_code
        team_dict['Prefix'] = team_prefix
        team_total.append(team_dict)
    # Write JSON file
    with open(file_name, 'w') as outfile:
        json.dump(team_total, outfile)
    with output:
        print("Team DB Updated, " + today)
    return

# Load team JSON file create above.
def data_set():
    data_filenames = [data_file for data_file in os.listdir() 
                      if data_file.endswith('.json')]
    with open(data_filenames[0]) as json_file:
        data = json.load(json_file)
    return data

# Gather league list for selection.
def league_names():
    league_list = []
    for x in data_set():
        if x['Competition'] is not None and x['Competition'] not in league_list:
            league_list.append(x['Competition'])
    return league_list[1:]

# Gather team list for selection.
def team_names(league_select):
    team_list = []
    for x in data_set():
        if x['Competition'] == league_select and x['Team'] not in team_list:
            team_list.append(x['Team'])
    return team_list

# Capture team details for parsing based on above choices.
def team_data(team_select):
    for x in data_set():
        if x['Team'] == team_select:
            return x

def parse_seasons(code,prefix,min_season):
    # Season to capture games for:
    season_to_parse = "https://fbref.com/en/squads/" + code + '/' + min_season + '/' + prefix
    # Parse season details.
    match_links = []
    season_page = bsoup(reqs.get(season_to_parse).content, 'html.parser')
    find_links = season_page.find_all('td',attrs={"data-stat":"match_report"})
    for x in find_links:
        add = x.find_next('a').attrs['href']
        match_links.append("https://fbref.com" + str(add))
    # Eventually change to game_data(match_links) to process game data.
    return game_data(match_links)

def game_data(match_links):
    from datetime import datetime
    all_matches = []
    match_dataset = {'Date': None, 'Home': None, 'Away': None, 
                     'Score Home': None,'Score Away': None,
                     'Manager Home': None, 'Manager Away': None,
                     'Captain Home': None, 'Captain Away': None,
                     'Attendance': None,
                     'Form Home': None, 'Form Away': None,
                     'Goals Home': None, 'Goals Away': None,
                     'Assists Home': None, 'Assists Away': None,
                     'Penalties Made Home': None, 'Penalties Made Away': None,
                     'Penalties Att Home': None, 'Penalties Att Away': None,
                     'Shots Total Home': None, 'Shots Total Away': None,
                     'SOT Home': None, 'SOT Away': None,
                     'Yellow Cards Home': None, 'Yellow Cards Away': None,
                     'Red Cards Home': None, 'Red Cards Away': None,
                     'Fouls Home': None, 'Fouls Away': None,
                     'Fouled Home': None, 'Fouled Away': None,
                     'Offsides Home': None, 'Offsides Away': None,
                     'Crosses Home': None, 'Crosses Away': None,
                     'Tackles Won Home': None, 'Tackles Won Away': None,
                     'Interceptions Home': None, 'Interceptions Away': None,
                     'Own Goals Home': None, 'Own Goals Away': None}
    for match in match_links:
        parse_page = bsoup(reqs.get(match).content, 'html.parser')
        # Date.
        find_date = parse_page.find("div",{"class":"scorebox_meta"}).find('a').get_text()
        date_adj = datetime.strptime(find_date[find_date.find(' ') + 1:], '%B %d, %Y')
        match_dataset['Date'] = date_adj.strftime('%Y-%m-%d')
        # Team names - capture from 'title'.
        find_teams = parse_page.find("title").get_text()
        match_dataset['Home'] = find_teams[:(find_teams.find('vs.') - 1)]
        match_dataset['Away'] = find_teams[(find_teams.find('vs.') + 4):find_teams.find('Match') - 1]
        # Score
        find_scores = parse_page.find_all("div",{"class":"score"})
        try:
            match_dataset['Score Home'] = int(find_scores[0].get_text())
            match_dataset['Score Away'] = int(find_scores[1].get_text())
        except:
            match_dataset['Score Home'] = None
            match_dataset['Score Away'] = None   
        # Managers
        find_leaders = parse_page.find_all("div",{"class":"datapoint"})
        for x in find_leaders:
            try:
                if x.get_text().find('Manager:') > -1 and match_dataset['Manager Home'] is None:
                    match_dataset['Manager Home'] = x.get_text().replace('\xa0', ' ').replace('Manager: ', '')
                elif x.get_text().find('Captain:') > -1 and match_dataset['Captain Home'] is None:
                    match_dataset['Captain Home'] = x.get_text().replace('\xa0', ' ').replace('Captain: ', '')
                elif x.get_text().find('Manager:') > -1 and match_dataset['Manager Home'] is not None:
                    match_dataset['Manager Away'] = x.get_text().replace('\xa0', ' ').replace('Manager: ', '')
                elif x.get_text().find('Captain:') > -1 and match_dataset['Captain Home'] is not None:
                    match_dataset['Captain Away'] = x.get_text().replace('\xa0', ' ').replace('Captain: ', '')
            except:
                match_dataset['Manager Home'] = None
                match_dataset['Manager Away'] = None
                match_dataset['Captain Home'] = None
                match_dataset['Captain Away'] = None
        # Attendance
        find_attend = parse_page.find_all("small")
        try:
            match_dataset['Attendance'] = int(find_attend[1].get_text().replace(',',''))
        except:
            match_dataset['Attendance'] = None
        # Formations
        find_form = parse_page.find_all('th', attrs={"colspan":"2"})
        try:
            match_dataset['Form Home'] = find_form[0].get_text().replace('◆','')
            match_dataset['Form Away'] = find_form[2].get_text().replace('◆','')
        except:
            match_dataset['Form Home'] = None
            match_dataset['Form Away'] = None
        # Add any new metrics here, before data addition.
        find_stats = parse_page.find_all('tfoot')
        all_stats = []
        for x in find_stats:
            try:
                all_stats.append(int(x.find('td',{'data-stat':'goals'}).get_text()))
            except:
                all_stats.append(0)
            try:    
                all_stats.append(int(x.find('td',{'data-stat':'assists'}).get_text()))
            except:
                all_stats.append(0)
            try:
                all_stats.append(int(x.find('td',{'data-stat':'pens_made'}).get_text()))
            except:
                all_stats.append(0)
            try:
                all_stats.append(int(x.find('td',{'data-stat':'pens_att'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'shots_total'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'shots_on_target'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'cards_yellow'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'cards_red'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'fouls'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'fouled'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'offsides'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'crosses'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'tackles_won'}).get_text()))
            except:
                all_stats.append(0)   
            try:
                all_stats.append(int(x.find('td',{'data-stat':'interceptions'}).get_text()))
            except:
                all_stats.append(0)    
            try:
                all_stats.append(int(x.find('td',{'data-stat':'own_goals'}).get_text()))
            except:
                all_stats.append(0)
        match_dataset['Goals Home'] = all_stats[0]
        match_dataset['Assists Home'] = all_stats[1]
        match_dataset['Penalties Made Home'] = all_stats[2]
        match_dataset['Penalties Att Home'] = all_stats[3]
        match_dataset['Shots Total Home'] = all_stats[4]
        match_dataset['SOT Home'] = all_stats[5]
        match_dataset['Yellow Cards Home'] = all_stats[6]
        match_dataset['Red Cards Home'] = all_stats[7]
        match_dataset['Fouls Home'] = all_stats[8]
        match_dataset['Fouled Home'] = all_stats[9]
        match_dataset['Offsides Home'] = all_stats[10]
        match_dataset['Crosses Home'] = all_stats[11]
        match_dataset['Tackles Won Home'] = all_stats[12]
        match_dataset['Interceptions Home'] = all_stats[13]
        match_dataset['Own Goals Home'] = all_stats[14]
        match_dataset['Goals Away'] = all_stats[15]
        match_dataset['Assists Away'] = all_stats[16]
        match_dataset['Penalties Made Away'] = all_stats[17]
        match_dataset['Penalties Att Away'] = all_stats[18]
        match_dataset['Shots Total Away'] = all_stats[19]
        match_dataset['SOT Away'] = all_stats[20]
        match_dataset['Yellow Cards Away'] = all_stats[21]
        match_dataset['Red Cards Away'] = all_stats[22]
        match_dataset['Fouls Away'] = all_stats[23]
        match_dataset['Fouled Away'] = all_stats[24]
        match_dataset['Offsides Away'] = all_stats[25]
        match_dataset['Crosses Away'] = all_stats[26]
        match_dataset['Tackles Won Away'] = all_stats[27]
        match_dataset['Interceptions Away'] = all_stats[28]
        match_dataset['Own Goals Away'] = all_stats[29]
        
        # Add game data to list.
        all_matches.append(match_dataset.copy())
        # Reset dict, as some values linger for some reason.
        match_dataset = {'Date': None, 'Home': None, 'Away': None, 
                     'Score Home': None,'Score Away': None,
                     'Manager Home': None, 'Manager Away': None,
                     'Captain Home': None, 'Captain Away': None,
                     'Attendance': None,
                     'Form Home': None, 'Form Away': None,
                     'Goals Home': None, 'Goals Away': None,
                     'Assists Home': None, 'Assists Away': None,
                     'Penalties Made Home': None, 'Penalties Made Away': None,
                     'Penalties Att Home': None, 'Penalties Att Away': None,
                     'Shots Total Home': None, 'Shots Total Away': None,
                     'SOT Home': None, 'SOT Away': None,
                     'Yellow Cards Home': None, 'Yellow Cards Away': None,
                     'Red Cards Home': None, 'Red Cards Away': None,
                     'Fouls Home': None, 'Fouls Away': None,
                     'Fouled Home': None, 'Fouled Away': None,
                     'Offsides Home': None, 'Offsides Away': None,
                     'Crosses Home': None, 'Crosses Away': None,
                     'Tackles Won Home': None, 'Tackles Won Away': None,
                     'Interceptions Home': None, 'Interceptions Away': None,
                     'Own Goals Home': None, 'Own Goals Away': None}
    return matches_to_file(all_matches)

def matches_to_file(all_matches):
    team = team_box.value.lower().replace(' ','_')
    season = season_box.value.replace('-','_')
    file_name = team + '_' + season + ".json"
    with open(file_name, 'w') as outfile:
        json.dump(all_matches, outfile)
    return print(file_name + " created")

### UI for league and team select
# Select league to pick team from.
try:
    league_box=Dropdown(
        options=league_names(),
        description='Pick League:',
        layout={'width': 'max-content'},
        style = {'description_width': 'initial'},
        disabled=False)

    # Select team to parse, and capture data for.
    team_box=Dropdown(
            description='Pick Team:',
            layout={'width': 'max-content'},
            style = {'description_width': 'initial'},
            disabled=False)

    # Select team to parse, and capture data for.
    season_box=Dropdown(
            description='Pick Season:',
    # 2014-2015 season is the earliest instance with match data from the looks of it.
            options=['2014-2015','2015-2016',
                    '2016-2017','2017-2018',
                    '2018-2019','2019-2020','2020-2021',
                    '2021-2022'],
            value='2019-2020',
            layout={'width': 'max-content'},
            style = {'description_width': 'initial'},
            disabled=False)

    scrape_button=Button(
            description='Update Team Data',
            style = {'description_width': 'initial'},
            disable=False)
    
    # Update DB if wanted.
    output = widgets.Output()
    display(scrape_button, output)
    scrape_button.on_click(team_capture)
    
    # UI interactives.
    @interact(league = league_box)
    def choose_both(league):
        team_box.options = team_names(league_box.value)
        return

    @interact_manual(team = team_box, use_season = season_box)
    def choose_team(team, use_season):
        return team_choice_cap(team_data(team),use_season)

    def team_choice_cap(data_set, use_season):
        code = data_set['Code']
        prefix = data_set['Prefix']
        return parse_seasons(code,prefix,use_season)

except:
    # Force DB update if no DB file present.
    print("No Team DB, click below and re-run script: \n")
    scrape_button=Button(
            description='Update Team Data',
            style = {'description_width': 'initial'},
            disable=False)
    output = widgets.Output()
    display(scrape_button, output)
    scrape_button.on_click(team_capture)
