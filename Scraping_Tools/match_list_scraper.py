# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/2018-2019/Northampton-Town
# To be combined fully with game_scraper.py

from bs4 import BeautifulSoup as bsoup
import requests as reqs

# Season used for file name - nothing fancy
page_to_parse = 'https://fbref.com/en/squads/986a26c1/2018-2019/Northampton-Town'

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
    
match_list= []

# Capture all match URLs from the main season
findinfo = parse_page.find_all('td',attrs={"data-stat":"match_report"})
for datum in findinfo:
    add_datum = datum.find_next('a').attrs['href']
    full_link = "https://fbref.com" + str(add_datum)
    match_list.append(str(full_link))
