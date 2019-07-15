# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Which season (YYYY format) to gen and, which URL to parse
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
season_numb = season_numb[0:10]

# Load data file to use
workbook_name = 'Ndata' + str(season_numb) + '.xlsx'
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
all_lists = [player_list,position_list,age_list,games_list,game_starts_list,game_subs_list,minutes_list,minutes_per_game_list, goals_list,assists_list,pens_made_list,pens_att_list,fouls_list,yellow_list,red_list,sot_list]
to_parse = ["player","position","age","games","game_starts","game_subs","minutes","minutes_per_game","goals","assists","pens_made","pens_att","fouls","cards_yellow","cards_red","shots_on_target"]

# Status notice
print("Creating dataset")
print("")

# Create playerlist - unique instances
findplayers = parse_page.find_all('th',attrs={"data-stat":"player"})
for player in findplayers:
    addplayer = player.find_next('a').get_text()
    if addplayer not in player_list and addplayer != 'coverage note':
        player_list.append(addplayer)

# Create positionlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'position'})
for position in findinfo:
    addposition = position.get_text()
    if addposition != 'coverage note':
        position_list.append(addposition)

# Create agelist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'age'})
for age in findinfo:
    addage = age.get_text()
    if addage != 'coverage note':
        age_list.append(addage)

# Create gameslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'games'})
for games in findinfo:
    addgames = games.get_text()
    if addgames != 'coverage note':
        games_list.append(addgames)

# Create gamestartlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'games_starts'})
for gamestart in findinfo:
    addstart = gamestart.get_text()
    if addstart != 'coverage note':
        game_starts_list.append(addstart)

# Create gamesubslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'games_subs'})
for subs in findinfo:
    addgamesubs = subs.get_text()
    if addgamesubs != 'coverage note':
        game_subs_list.append(addgamesubs)

# Create minuteslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'minutes'})
for mins in findinfo:
    addminutes = mins.get_text()
    if addminutes != 'coverage note':
        minutes_list.append(addminutes)

# Create minutespgamelist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'minutes_per_game'})
for minsp in findinfo:
    addminutespgame = minsp.get_text()
    if addminutespgame != 'coverage note':
        minutes_per_game_list.append(addminutespgame)

# Create goalslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'goals'})
for goals in findinfo:
    addgoals = goals.get_text()
    if addgoals != 'coverage note':
        goals_list.append(addgoals)

# Create assistslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'assists'})
for assists in findinfo:
    addassists =  assists.get_text()
    if addassists != 'coverage note':
        assists_list.append(addassists)

# Create pensmadelist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'pens_made'})
for pens in findinfo:
    addpensmade = pens.get_text()
    if addpensmade != 'coverage note':
        pens_made_list.append(addpensmade)

# Create pensattlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'pens_att'})
for pensa in findinfo:
    addpensatt = pensa.get_text()
    if addpensatt != 'coverage note':
        pens_att_list.append(addpensatt)

# Create foulslist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'fouls'})
for fouls in findinfo:
    addfouls = fouls.get_text()
    if addfouls != 'coverage note':
        fouls_list.append(addfouls)

# Create yellowlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'cards_yellow'})
for yellow in findinfo:
    addyellow = yellow.get_text()
    if addyellow != 'coverage note':
        yellow_list.append(addyellow)

# Create redlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'cards_red'})
for red in findinfo:
    addred = red.get_text()
    if addred != 'coverage note':
        red_list.append(addred)

# Create sotlist - non-unique
findinfo = parse_page.find_all('td',attrs={"data-stat":'shots_on_target'})
for sot in findinfo:
    addsot = sot.get_text()
    if addsot != 'coverage note':
        sot_list.append(addsot)

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

# Fill data points into set
startrow = 1
startcol = 0
for lst in all_lists:
    for var in lst:
        worksheet.write(startrow, startcol, var)
        startrow += 1
    startrow = 1
    startcol = startcol + 1

# Finish Excel creation
workbook.close()

# Status notice
print(str(workbook_name) + " created successfully")
