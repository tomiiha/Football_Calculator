# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs

# Capture website
page = reqs.get("https://fbref.com/en/squads/986a26c1/Northampton-Town")
status = page.status_code
parsepage = bsoup(page.content, 'html.parser')

# Lists
playerlist = []
positionlist = []
agelist = []
gamesplayedlist = []
gamestartslist = []
gamesubslist = []
minuteslist = []
minutespgamelist = []

# Elements to ultimately find in toparse - gen player list off of findplayers
toparse = ["player","position","age","games","game_starts","game_subs","minutes","minutes_per_game"]
findplayers = parsepage.find_all('th',attrs={"data-stat":"player"})
for name in findplayers:
    playerlist.append(player)
    print(player.find_next('a').get_text())
