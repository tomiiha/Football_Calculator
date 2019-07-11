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

# Capture website
pagetoparse = 'https://fbref.com/en/squads/986a26c1/Northampton-Town'
page = reqs.get(pagetoparse)
status = page.status_code
parsepage = bsoup(page.content, 'html.parser')

# Status notice
print("Parsing: " + str(pagetoparse))

# Lists
playerlist = []
positionlist = []
agelist = []
gamesplayedlist = []
gamestartslist = []
gamesubslist = []
minuteslist = []
minutespgamelist = []

# Status notice
print("Creating dataset")

# Elements to ultimately find in toparse - gen player list off of findplayers
# Actual toparse list below, enact for full dataset build
#toparse = ["player","position","age","games","game_starts","game_subs","minutes","minutes_per_game"]
toparse = ["player"]
findplayers = parsepage.find_all('th',attrs={"data-stat":toparse})
for player in findplayers:
    addplayer = player.find_next('a').get_text()
    if addplayer not in playerlist and addplayer != 'coverage note':
        playerlist.append(addplayer)

# Status notice
print("Dataset created - adding to Excel sheet")

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
print(str(workbookname + " created successfully")
