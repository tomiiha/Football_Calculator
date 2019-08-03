# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Define what team we want the data for
team_to_scrape = "Northampton Town"

# Season used for file name - nothing fancy
page_to_parse = 'https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two'

# Capture website
page = reqs.get(page_to_parse)
status_code = page.status_code
status_code = str(status_code)
parse_page = bsoup(page.content, 'html.parser')

# Status notice - stat_comp should start with 2 for parsing to have been completed
stat_comp = "2"
if status_code[0] == stat_comp:
    print("Parsing: " + str(page_to_parse) + " completed")
    print("")
else:
    print("There might have been an issue with parsing")
    print("")
    
# Lists
team_list = []
score_list = []
manager_list = []
stat_list = []
foul_list = []

# Capture team names (index 0 is home, index 1 is away)
team_names = parse_page.find_all("div", itemprop="performer")
for team in team_names:
    add_team = team.find_next('a').get_text()
    team_list.append(str(add_team))

# Team name lengths for data clean-up
home_len = len(team_list[0])
away_len = len(team_list[1])
    
# Considering all data is split left-right
# Below chooses the data for the right team per team_to_scrape
if team_list[0] == team_to_scrape:
    data_index = 0
elif team_list[1] == team_to_scrape:
    data_index = 1
    
# Test data indexing to determine data 'side' on page
#print(team_list[data_index])
#print(score_list[data_index])

# Capture game score
game_scores = parse_page.find_all("td",{"class":"score"})
for score in game_scores:
    add_score = score.get_text()
    score_list.append(int(add_score))

fouls_len = len("fouls")
find_fouls = parse_page.find_all('div',id="team_stats_extra")
for stat in find_fouls:
    add_foul = stat.find_next('div').get_text()
    add_foul = add_foul[(home_len + away_len - 2):]
    add_foul = add_foul[:add_foul.find('\n')]
    add_foul_home = add_foul[:add_foul.find("Fouls")]
    add_foul_away = add_foul[(add_foul.find("Fouls") + fouls_len):]
    stat_list.append(add_foul_home)
    stat_list.append(add_foul_away)
