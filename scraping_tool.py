# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Season used for file name - nothing fancy
page_to_parse = 'https://fbref.com/en/squads/986a26c1/Northampton-Town'

# Capture website
page = reqs.get(page_to_parse)
status_code = page.status_code
status_code = str(status_code)
parse_page = bsoup(page.content, 'html.parser')

# Capture season number
season_numb = parse_page.find('h1')
season_numb = season_numb.get_text()
season_numb = season_numb[1:10]

# Load data file to use
workbook_name = r'Data\NData' + str(season_numb) + '.xlsx'
workbook = xsl.Workbook(workbook_name)
worksheet = workbook.add_worksheet()

# Status notice
print("Workbook " + str(workbook_name) + " created")
print("")

# Status notice - stat_comp should start with 2 for parsing to have been completed
stat_comp = "2"
if status_code[0] == stat_comp:
    print("Parsing: " + str(page_to_parse) + " completed")
    print("")
else:
    print("There was an issue with parsing")
    print("")

# Lists
player_list = []
position_list = []
age_list = []
games_list = []
game_starts_list = []
game_subs_list = []
minutes_list = []
minutes_per_game_list = []
goals_list = []
assists_list = []
pens_made_list = []
pens_att_list = []
fouls_list = []
yellow_list = []
red_list = []
sot_list = []

# Excel lists
all_list = [player_list,position_list,age_list,games_list,game_starts_list,game_subs_list,minutes_list,minutes_per_game_list, goals_list,assists_list,pens_made_list,pens_att_list,fouls_list,yellow_list,red_list,sot_list]
to_parse = ["player","position","age","games","games_starts","games_subs","minutes","minutes_per_game","goals","assists","pens_made","pens_att","fouls","cards_yellow","cards_red","shots_on_target"]

# Status notice
print("Creating dataset")
print("")

# Create playerlist - unique instances
findplayers = parse_page.find_all('th',attrs={"data-stat":"player"})
for player in findplayers:
    addplayer = player.find_next('a').get_text()
    if addplayer not in player_list and addplayer != 'coverage note':
        player_list.append(addplayer)

# Grab website data
grab_list = 0
for data_point in to_parse:
	findinfo = parse_page.find_all('td',attrs={"data-stat":data_point})
	for datum in findinfo:
		add_datum = datum.get_text()
		if add_datum != 'coverage note':
			all_list[grab_list].append(add_datum)
	grab_list = grab_list + 1

# Status notice
print("Dataset created - adding to Excel sheet")
print("")

# Data writing into excel file
# Create headers based on col_headers
startrow = 0
startcol = 0
for header in to_parse:
    worksheet.write(startrow, startcol, header)
    startcol += 1

# Fill data points into set per player count (to remove totals)
player_count = len(player_list)
startrow = 1
startcol = 0
for lst in all_list:
    for var in lst[:int(player_count)]:
        worksheet.write(startrow, startcol, var)
        startrow += 1
    startrow = 1
    startcol = startcol + 1

# Finish Excel creation
workbook.close()

# Status notice
print(str(workbook_name) + " created successfully")
