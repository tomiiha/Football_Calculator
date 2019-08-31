# Note: https://fbref.com/robots.txt
# Home test: https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two
# Away test: https://fbref.com/en/matches/ea736ad1/Carlisle-United-Northampton-Town-August-11-2018-League-Two

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl
import re

# Define what team we want the data for
team_to_scrape = "Northampton Town"

# Season used for file name - nothing fancy
home_tests = ["https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two", "https://fbref.com/en/matches/e5590f2e/Northampton-Town-Cambridge-United-August-18-2018-League-Two"]
away_tests = ["https://fbref.com/en/matches/ea736ad1/Carlisle-United-Northampton-Town-August-11-2018-League-Two", "https://fbref.com/en/matches/46c9cbcb/Morecambe-Northampton-Town-August-21-2018-League-Two"]

# Choose home or away game from lists above - indices 0-1
page_to_parse = away_tests[1]

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
foul_list = []
corner_list = []
cross_list = []
touch_list = []
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
    
# Capture game_date
find_date = parse_page.find("h1")
add_date = find_date.get_text()
for date in weekday_list:
    if add_date.find(date) != -1:
        date_pos = add_date.find(date)
        date_len = len(date)
        game_date = add_date[(date_pos + date_len + 1):]

# Capture game score
game_scores = parse_page.find_all("div",{"class":"score"})
for score in game_scores:
    add_score = score.get_text()
    score_list.append(int(add_score))
    
# Capture managers (remove captains)
game_manager = parse_page.find_all("div",{"class":"datapoint"})
for manager in game_manager:
    add_manager = manager.get_text()
    if "Captain:" not in add_manager:    
        manager_list.append(str(add_manager[9:]))
        
# Find teams for removal (as they differ at times from the main ones), add to list
find_stats = parse_page.find_all('div',{'class':'th'})
for stat in find_stats:
    add_stat = stat.get_text()
    temp_list.append(add_stat)
team_one_len = len(temp_list[0])
team_two_len = len(temp_list[2])
    
# Stats are broken down into two divs in the page, list of these elements
extra_stats = ["Fouls","Corners","Crosses","Touches"]
working_stat = extra_stats[0]
stat_len = len(working_stat)

# Find stat locations for parsing
find_fouls = parse_page.find_all('div',id="team_stats_extra")
for stat in find_fouls:
    add_stats = stat.find_next('div').get_text()
    add_stats = add_stats[(add_stats.find('\n') + 1):]
    add_stats = add_stats[(team_one_len + team_two_len + 2):]
    index_list = [m.start() for m in re.finditer('\n', str(add_stats))]

temp_stat_list.append(add_stats[:(index_list[0])])
temp_stat_list.append(add_stats[index_list[1] + 1:index_list[2]])
temp_stat_list.append(add_stats[index_list[2] + 1:index_list[3]])
print(temp_stat_list)
