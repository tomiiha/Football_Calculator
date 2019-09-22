# Note: https://fbref.com/robots.txt
# Season capture example: https://fbref.com/en/squads/986a26c1/2018-2019/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Define what team we want the data for
team_to_scrape = "Northampton Town"

# URL for season to capture
season_to_parse = 'https://fbref.com/en/squads/986a26c1/2018-2019/Northampton-Town'
season_numb = "2018-2019"

# Capture the season overview page
page = reqs.get(season_to_parse)
status_code = page.status_code
status_code = str(status_code)
season_page = bsoup(page.content, 'html.parser')

match_list = []
stat_rows = ["Date","Team","Manager","Score","Fouls","Corners","Crosses","Touches","Clearances","Offsides","Goal Kicks","Throw Ins","Long Balls","Possession","Shots on Goal","Shots","Shots on Goal Conc","Shots Conc","Saves"]

# Capture all match URLs from the main season
findinfo = season_page.find_all('td',attrs={"data-stat":"match_report"})
for datum in findinfo:
    add_datum = datum.find_next('a').attrs['href']
    full_link = "https://fbref.com" + str(add_datum)
    match_list.append(str(full_link))

print(season_to_parse + ": Season matches captured")

# Load data file to use
workbook_name = "Data " + team_to_scrape + " Season Games "  + str(season_numb) + '.xlsx'
workbook = xsl.Workbook(workbook_name)
worksheet = workbook.add_worksheet()

# Status notice
print("Workbook " + str(workbook_name) + " created")
print("")

# Create row headers for excel file
startrow = 0
startcol = 0
for val in stat_rows:
    worksheet.write(startrow, startcol, str(val))
    startrow += 1
startcol += 1

# Grab game from match_list, for testing purposes for now without running the full list
# Remove list indices to run full season
num_matches = len(match_list)
for match in match_list:
    page_to_parse = match
    
# Capture game page from match_list
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

# Lists, also placed for clearing each instance
    team_list = []
    score_list = []
    manager_list = []
    foul_list = []
    corner_list = []
    cross_list = []
    touch_list = []
    clearance_list = []
    offside_list = []
    goal_kick_list = []
    throw_in_list = []
    long_ball_list = []
    possession_list = []
    shots_list = []
    sot_list = []
    save_list = []
    shots_conc_list = []
    sot_conc_list = []
    other_stat_list = []
    
# Temporary lists for parsing
    other_temp_list = []
    temp_list = []
    temp_stat_list = []

# weekday_list used for date capture
    weekday_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# Capture team names (index 0 is home, index 1 is away)
    team_names = parse_page.find_all("div", itemprop="performer")
    for team in team_names:
        add_team = team.find_next('a').get_text()
        team_list.append(str(add_team))

# Team name lengths for data clean-up
    home_len = len(team_list[0])
    away_len = len(team_list[1])

# Considering all data is split left-right
# Below chooses the data for the right team per team_to_scrape
    if team_list[0] == team_to_scrape:
        team_index = 0
    elif team_list[1] == team_to_scrape:
        team_index = 1

# Capture game date
    find_date = parse_page.find("h1")
    add_date = find_date.get_text()
    for date in weekday_list:
        if add_date.find(date) != -1:
            date_pos = add_date.find(date)
            date_len = len(date)
            game_date = add_date[(date_pos + date_len + 1):]

# Capture game score
    game_scores = parse_page.find_all("div",{"class":"score"})
    for score in game_scores:
        add_score = score.get_text()
        score_list.append(int(add_score))

# Capture managers (remove captains)
    game_manager = parse_page.find_all("div",{"class":"datapoint"})
    for manager in game_manager:
        add_manager = manager.get_text()
        if "Captain:" not in add_manager:
            manager_list.append(str(add_manager[9:]))

# Find teams for removal (as they differ at times from the main ones), add to list
    find_stats = parse_page.find_all('div',{'class':'th'})
    for stat in find_stats:
        add_stat = stat.get_text()
        temp_list.append(add_stat)
    team_one_len = len(temp_list[0])
    team_two_len = len(temp_list[2])
    
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

# Parse home Saves and SOT Conceded
    saving_home = other_temp_list[4]
    saving_home = saving_home[:saving_home.find('\xa0')]
    sot_conc_home = saving_home[(saving_home.find('of') + 3):]
    saves_home = saving_home[:(saving_home.find('of') - 1)]
    save_list.append(int(saves_home))
    sot_conc_list.append(int(sot_conc_home))

# Parse away Saves and SOT Conceded
    saving_away = other_temp_list[5]
    saving_away = saving_away[(saving_away.find('\xa0') + 1):]
    sot_conc_away = saving_away[(saving_away.find('of') + 3):]
    saves_away = saving_away[:(saving_away.find('of') - 1)]
    save_list.append(int(saves_away))
    sot_conc_list.append(int(sot_conc_away))
    
# Gather shots conceded from team_index, and respective opposite away/home stats
    if team_index == 0:
        shots_conc_list.append(shots_away)
        shots_conc_list.append(shots_home)
    elif team_index == 1:
        shots_conc_list.append(shots_home)
        shots_conc_list.append(shots_away)

# Capture match data details in text, to prep for parsing
    find_stats = parse_page.find_all('div', id="team_stats_extra")
    all_stats = find_stats[0].find_all('div', recursive=False)
    for stat in all_stats:
        temp_stat_list.append(stat.get_text())
    add_stats = ''.join(temp_stat_list)
        
# Parse individual statistics from the string - separate line breaks, and form into list
# Also remove empty entries
    removal = temp_list[0] + temp_list[2]
    add_stats = add_stats.replace(u'\xa0', u'')
    add_stats = add_stats.split('\n')
    add_stats = list(filter(None, add_stats))
    while removal in add_stats:
        add_stats.remove(removal)

# Parse above created list, and assign game statistics to appropriate lists per dictionary
    extra_stats_dict = {"Score":score_list,"Fouls":foul_list,"Corners":corner_list,"Crosses":cross_list,"Touches":touch_list,"Clearances":clearance_list,"Offsides":offside_list,"Goal Kicks":goal_kick_list,"Throw Ins":throw_in_list,"Long Balls":long_ball_list,"Possession":possession_list,"Shots on Goal":sot_list,"Shots":shots_list,"Shots on Goal Conceded":sot_conc_list,"Shots Conceded":shots_conc_list,"Saves":save_list}
    for key in extra_stats_dict:
        for val in add_stats:
            if key in val:
                stat_home = val[:val.find(key)]
                stat_away = val[(val.find(key) + len(key)):]
                extra_stats_dict[key].append(int(stat_home))
                extra_stats_dict[key].append(int(stat_away))

# Not all statistics are in place for all games
# Below to check all lists, and apply 0 to unpopulated statistics 
    for y, x in extra_stats_dict.items():
        if len(x) == 0:
            x.append(0)
            x.append(0)

# Add data to columns by game
    startrow = 0
    worksheet.write(startrow, startcol, str(game_date))
    startrow += 1
    worksheet.write(startrow, startcol, str(team_list[team_index]))
    startrow += 1
    worksheet.write(startrow, startcol, str(manager_list[team_index]))
    startrow += 1
    for z, p in extra_stats_dict.items():
        worksheet.write(startrow, startcol, int(p[team_index]))
        startrow += 1
    startcol += 1

# Finish Excel creation
workbook.close()

# Status notice
print(str(workbook_name) + " created successfully")
