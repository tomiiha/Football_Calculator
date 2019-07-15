# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Which season (YYYY format) to gen and, which URL to parse
# Season used for file name - nothing fancy
season = 1819
pagetoparse = 'https://fbref.com/en/squads/986a26c1/Northampton-Town'

# Load data file to use
workbookname = 'Ndata' + str(season) + '.xlsx'
workbook = xsl.Workbook(workbookname)
worksheet = workbook.add_worksheet()

# Status notice
print("Workbook " + str(workbookname) + " created")
print("")

# Capture website
page = reqs.get(pagetoparse)
statuscode = page.status_code
statuscode = str(statuscode)
statcomp = "2"
parsepage = bsoup(page.content, 'html.parser')

# Status notice
if statuscode[0] == statcomp:
    print("Parsing: " + str(pagetoparse) + " completed")
    print("")
else:
    print("There was an issue with parsing")
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
goalslist = []
assistslist = []
pensmadelist = []
pensattlist = []
foulslist = []
yellowlist = []
redlist = []
sotlist = []

# Excel lists
all_lists = [playerlist,positionlist,agelist,gameslist,gamestartslist,gamesubslist,minuteslist,minutespgamelist, goalslist,assistslist,pensmadelist,pensattlist,foulslist,yellowlist,redlist,sotlist]
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

# Create agelist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'age'})
for age in findinfo:
    addage = age.get_text()
    if addage != 'coverage note':
        agelist.append(addage)

# Create gameslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'games'})
for games in findinfo:
    addgames = games.get_text()
    if addgames != 'coverage note':
        gameslist.append(addgames)

# Create gamestartlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'game_starts'})
for gamestart in findinfo:
    addstart = gamestart.get_text()
    if addstart != 'coverage note':
        gamestartslist.append(addstart)

# Create gamesubslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'game_subs'})
for subs in findinfo:
    addgamesubs = subs.get_text()
    if addgamesubs != 'coverage note':
        gamesubslist.append(addgamesubs)

# Create minuteslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'minutes'})
for mins in findinfo:
    addminutes = mins.get_text()
    if addminutes != 'coverage note':
        minuteslist.append(addminutes)

# Create minutespgamelist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'minutes_per_game'})
for minsp in findinfo:
    addminutespgame = minsp.get_text()
    if addminutespgame != 'coverage note':
        minutespgamelist.append(addminutespgame)
        
# Create goalslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'assists'})
for goals in findinfo:
    addgoals = goals.get_text()
    if addgoals != 'coverage note':
        goalslist.append(addgoals)
        
# Create assistslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'assists'})
for assists in findinfo:
    addassists =  assists.get_text()
    if addassists != 'coverage note':
        assistslist.append(addassists)
        
# Create pensmadelist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'pens_made'})
for pens in findinfo:
    addpensmade = pens.get_text()
    if addpensmade != 'coverage note':
        pensmadelist.append(addpensmade)
        
# Create pensattlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'pens_att'})
for pensa in findinfo:
    addpensatt = pensa.get_text()
    if addpensatt != 'coverage note':
        pensattlist.append(addpensatt)
        
# Create foulslist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'fouls'})
for fouls in findinfo:
    addfouls = fouls.get_text()
    if addfouls != 'coverage note':
        foulslist.append(addfouls)
        
# Create yellowlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'cards_yellow'})
for yellow in findinfo:
    addyellow = yellow.get_text()
    if addyellow != 'coverage note':
        yellowlist.append(addyellow)
        
# Create redlist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'cards_red'})
for red in findinfo:
    addred = red.get_text()
    if addred != 'coverage note':
        redlist.append(addred)
        
# Create minutespgamelist - non-unique
findinfo = parsepage.find_all('td',attrs={"data-stat":'shots_on_target'})
for sot in findinfo:
    addsot = sot.get_text()
    if addsot != 'coverage note':
        sotlist.append(addsot)
            
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
for lst in all_lists:
    for var in lst:
        worksheet.write(startrow, startcol, var)
        startrow += 1
    startrow = 0
    startcol = startcol + 1


# Finish Excel creation
workbook.close()

# Status notice
print(str(workbookname) + " created successfully")
