# Note: https://fbref.com/robots.txt
# Home test: https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two
# Away test: https://fbref.com/en/matches/ea736ad1/Carlisle-United-Northampton-Town-August-11-2018-League-Two

from bs4 import BeautifulSoup as bsoup
import requests as reqs

# Define what team we want the data for
team_to_scrape = "Northampton Town"

# Season used for file name - nothing fancy
home_test = "https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two"
away_test = "https://fbref.com/en/matches/ea736ad1/Carlisle-United-Northampton-Town-August-11-2018-League-Two"

# Choose home or away game from lists above - indices 0-1
page_to_parse = home_test

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
possession_list = []
manager_list = []
foul_list = []
corner_list = []
cross_list = []
touch_list = []
offside_list = []
goal_kick_list = []
throw_in_list = []
long_ball_list = []
temp_list = []
temp_stat_list = []

# weekday_list used for date capture
weekday_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

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
    team_index = 0
elif team_list[1] == team_to_scrape:
    team_index = 1

# Capture game score
game_other_stats = parse_page.find_all("div",id="team_stats")
print(game_other_stats)
for pos in game_other_stats:
    add_possession = pos.find_next('td').get_text()
    print(add_possession)
    possession_list.append(add_possession)
    
print(possession_list)
