# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Load data file to use
workbookname = 'Ndata1819.xlsx'
workbook = xsl.Workbook(workbookname)
worksheet = workbook.add_worksheet()

# Status notice
print("Workbook " + str(workbookname) + " created")
print("")

# Capture website
pagetoparse = 'https://fbref.com/en/squads/986a26c1/Northampton-Town'
page = reqs.get(pagetoparse)
status = page.status_code
parsepage = bsoup(page.content, 'html.parser')

# Status notice
print("Parsing: " + str(pagetoparse))
print("")

# Lists
playerlist = []
positionlist = []
agelist = []
gameslist = []
gamestartslist = []
gamesubslist = []
minuteslist = []
minutespgamelist = []
toparse = ["player","position","age","games","game_starts","game_subs","minutes","minutes_per_game"]

# Status notice
print("Creating dataset")
print("")

# Create playerlist - unique instances
findplayers = parsepage.find_all('th',attrs={"data-stat":"player"})
for player in findplayers:
    addplayer = player.find_next('a').get_text()
    if addplayer not in playerlist and addplayer != 'coverage note':
        playerlist.append(addplayer)
            
# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'position'})
for position in findinfo:
    addposition = position.get_text()
    if addposition != 'coverage note':
        positionlist.append(addposition)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'age'})
for age in findinfo:
    addage = age.get_text()
    if addage != 'coverage note':
        agelist.append(addage)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'games'})
for games in findinfo:
    addgames = games.get_text()
    if addgames != 'coverage note':
        gameslist.append(addgames)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'game_starts'})
for gamestart in findinfo:
    addstart = gamestart.get_text()
    if addstart != 'coverage note':
        gamestartslist.append(addstart)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'game_subs'})
for subs in findinfo:
    addgamesubs = subs.get_text()
    if addgamesubs != 'coverage note':
        gamesubslist.append(addgamesubs)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'minutes'})
for mins in findinfo:
    addminutes = mins.get_text()
    if addminutes != 'coverage note':
        minuteslist.append(addminutes)

# Create positionlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'minutes_per_game'})
for minsp in findinfo:
    addminutespgame = minsp.get_text()
    if addminutespgame != 'coverage note':
        minutespgamelist.append(addminutespgame)
            
# Status notice
print("Dataset created - adding to Excel sheet")
print("")

# Data writing into excel file - insert lists to designated columns A1 onward
startrow = 0
startcol = 0
for header in toparse:
    worksheet.write(startrow, startcol, header)
    startcol += 1
startrow = 1
startcol = 0
for player in addplayer:
    worksheet.write(startrow, startcol, player)
    startrow += 1
workbook.close()

# Status notice
print(str(workbookname) + " created successfully")
