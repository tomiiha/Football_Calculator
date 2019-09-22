from bs4 import BeautifulSoup as bsoup
import requests as reqs

other_stat_list = []
other_temp_list = []

page_to_parse = 'https://fbref.com/en/matches/033092ef/Northampton-Town-Lincoln-City-August-4-2018-League-Two'

page = reqs.get(page_to_parse)
parse_page = bsoup(page.content, 'html.parser')


find_other_stats = parse_page.find('div', id="team_stats")
for val in find_other_stats.find_all('td'):
    add_other_stats = val.get_text(strip=True)
    other_temp_list.append(add_other_stats)

print(other_temp_list)
