# Create new parse for possession, sot, saves totals
newparse <div id="team_stats"> for <div><strong>58%</strong></div>

from bs4 import BeautifulSoup as bsoup
import requests as reqs

other_stat_list = []

page_to_parse = 'https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two'
    
page = reqs.get(season_to_parse)
status_code = page.status_code
status_code = str(status_code)
parse_page = bsoup(page.content, 'html.parser')

find_other_stats = parse_page.find_all('div', id="team_stats_extra")
all_other_stats = find_other_stats[0].find_all('div', recursive=False)
for stat in all_other_stats:
    add_other_stats = find_next('strong').get_text()
     other_stat_list.append(add_team)

print(other_stat_list)
