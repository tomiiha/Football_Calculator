# Packaged used across functions - others in respective functions.
from bs4 import BeautifulSoup as bsoup
import requests as reqs
import json
import os
import ipywidgets as widgets

# team_capture to be used to generate a list of teams
def team_capture():
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
    return file_name

# Gather team list for selection.
def team_names():
    team_list = []
    data_filenames = [data_file for data_file in os.listdir()
              if data_file.endswith('.json')]
    return team_list

# Capture team details for season parsing.
def team_code(team_select):
    data_filenames = [data_file for data_file in os.listdir()
              if data_file.endswith('.json')]
    with open(data_filenames[0]) as json_file:
        data = json.load(json_file)
        for x in data:
            if x['Team'] == team_select:
                return x['Code']

def parse_seasons():
    # Season to capture games for:
    season_to_parse = "https://fbref.com/en/squads/986a26c1/2019-2020/Northampton-Town-Stats"
    # Parse season details.
    match_links = []
    season_page = bsoup(reqs.get(season_to_parse).content, 'html.parser')
    find_links = season_page.find_all('td',attrs={"data-stat":"match_report"})
    for x in find_links:
        add = x.find_next('a').attrs['href']
        match_links.append("https://fbref.com" + str(add))
    return game_data(match_links)

def game_data(match_links):
    from datetime import datetime
    match_dataset = {}
    for match in match_links[:1]:
        parse_page = bsoup(reqs.get(match).content, 'html.parser')
        # Date.
        find_date = parse_page.find("div",{"class":"scorebox_meta"}).find('a').get_text()
        date_adj = datetime.strptime(find_date[find_date.find(' ') + 1:], '%B %d, %Y')
        match_dataset['Date'] = date_adj.strftime('%Y-%m-%d')
        # Team names - capture from 'title'.
        find_teams = parse_page.find("title").get_text()
        match_dataset['Home'] = find_teams[:(find_teams.find('vs.') - 1)]
        match_dataset['Away'] = find_teams[(find_teams.find('vs.') + 4):find_teams.find('Match') - 1]
        # Score.
        find_scores = parse_page.find_all("div",{"class":"score"})
        print(find_scores)
    return

# Run the whole gambit
# parse_seasons()
# team_capture()
# team_select = 'Northampton Town FC'
# team_code(team_select)
