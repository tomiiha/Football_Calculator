from bs4 import BeautifulSoup as bsoup
import requests as reqs

other_stat_list = []
other_temp_list = []
possession_list = []
sot_list = []
sot_conc_list = []
shots_list = []
shots_conc_list = []
save_list = []

page_to_parse = 'https://fbref.com/en/matches/e5590f2e/Northampton-Town-Cambridge-United-August-18-2018-League-Two'

page = reqs.get(page_to_parse)
parse_page = bsoup(page.content, 'html.parser')


find_other_stats = parse_page.find('div', id="team_stats")
for val in find_other_stats.find_all('td'):
    add_other_stats = val.get_text(strip=True)
    other_temp_list.append(add_other_stats)

# Parse possession
poss_home = other_temp_list[0]
poss_home = poss_home[:poss_home.find('%')]
possession_list.append(int(poss_home))
poss_away = other_temp_list[1]
poss_away = poss_away[:poss_away.find('%')]
possession_list.append(int(poss_away))

# Parse home Shots and SOT
shooting_home = other_temp_list[2]
shooting_home = shooting_home[:shooting_home.find('\xa0')]
shots_home = shooting_home[(shooting_home.find('of') + 3):]
sot_home = shooting_home[:(shooting_home.find('of') - 1)]
shots_list.append(int(shots_home))
sot_list.append(int(sot_home))

# Parse home Shots and SOT
shooting_away = other_temp_list[3]
shooting_away = shooting_away[(shooting_away.find('\xa0') + 1):]
shots_away = shooting_away[(shooting_away.find('of') + 3):]
sot_away = shooting_away[:(shooting_away.find('of') - 1)]
shots_list.append(int(shots_away))
sot_list.append(int(sot_away))

# Parse home Saves and Goals Conceded
saving_home = other_temp_list[4]
saving_home = saving_home[:saving_home.find('\xa0')]
sot_conc_home = saving_home[(saving_home.find('of') + 3):]
saves_home = saving_home[:(saving_home.find('of') - 1)]
save_list.append(int(saves_home))
sot_conc_list.append(int(sot_conc_home))

# Parse away Saves and Goals Conceded
saving_away = other_temp_list[5]
saving_away = saving_away[(saving_away.find('\xa0') + 1):]
sot_conc_away = saving_away[(saving_away.find('of') + 3):]
saves_away = saving_away[:(saving_away.find('of') - 1)]
save_list.append(int(saves_away))
sot_conc_list.append(int(sot_conc_away))

print(possession_list)
print(sot_list)
print(shots_list)
print(save_list)
print(sot_conc_list)
