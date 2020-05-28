# Season capture example: https://fbref.com/en/squads/986a26c1/2018-2019/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import json

def season_list(team_to_scrape, season_to_scrape):
    match_list = []
    season_to_parse = "https://fbref.com/en/squads/986a26c1/" + season_to_scrape + team_to_scrape.replace(' ','-')
    page = reqs.get(season_to_parse)
    season_page = bsoup(page.content, 'html.parser')
    find_info = season_page.find_all('td',attrs={"data-stat":"match_report"})
    for datum in find_info:
        add_datum = datum.find_next('a').attrs['href']
        full_link = "https://fbref.com" + str(add_datum)
        match_list.append(str(full_link))
    return match_list

def match_parser(match_list):
    for link in match_list[0:1]:
        page = reqs.get(link)
        parse_page = bsoup(page.content, 'html.parser')
    return parse_page

def data_cap(parse_page):
    return -1

def json_export(var):
    return -1

# Processing
team_to_scrape = "Northampton Town"
season_to_scrape = "2018-2019"
match_list = season_list(team_to_scrape, season_to_scrape)
print(match_parser(match_list))
