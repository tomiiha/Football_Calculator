# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/comps/16/League-Two-Stats

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# League page
page_to_parse = 'https://fbref.com/en/comps/16/League-Two-Stats'

# Capture website
page = reqs.get(page_to_parse)
status_code = page.status_code
status_code = str(status_code)
parse_page = bsoup(page.content, 'html.parser')

# Capture season number
season_name = parse_page.find('h1')
season_name = season_name.get_text()

# Load data file to use
workbook_name = str(season_name) + '.xlsx'
workbook = xsl.Workbook(workbook_name)
worksheet = workbook.add_worksheet()

# Status notice
print("Workbook " + workbook_name + " created")
print("")

# Status notice - stat_comp should start with 2 for parsing to have been completed
stat_comp = "2"
if status_code[0] == stat_comp:
    print("Parsing: " + str(page_to_parse) + " completed")
    print("")
else:
    print("There was an issue with parsing")
    print("")

# Lists
squad_list = []
games_list = []
wins_list = []
draws_list = []
losses_list = []
goals_for_list = []
goals_against_list = []
goal_diff_list = []
points_list = []

# Excel lists
all_list = [squad_list,games_list,wins_list,draws_list,losses_list,goals_for_list,goals_against_list,points_list]
to_parse = ["squad","games","wins","draws","losses","goals_for","goals_against","goal_diff","points"]

# Status notice
print("Creating dataset")
print("")

grab_list = 0
for data_point in to_parse:
	findinfo = parse_page.find_all('td',attrs={"data-stat":data_point})
	for datum in findinfo:
		add_datum = datum.get_text()
		if add_datum != 'coverage note':
			all_list[grab_list].append(add_datum)
	grab_list = grab_list + 1

# Status notice
print("Dataset created - adding to Excel sheet")
print("")

# Data writing into excel file
# Create headers based on col_headers
startrow = 0
startcol = 0
for header in to_parse:
    worksheet.write(startrow, startcol, header)
    startcol += 1

# Fill data points into set per player count (to remove totals)
squad_count = len(squad_list)
startrow = 1
startcol = 0
for lst in all_list:
    for var in lst[:int(squad_count)]:
        worksheet.write(startrow, startcol, var)
        startrow += 1
    startrow = 1
    startcol = startcol + 1

# Finish Excel creation
workbook.close()

# Status notice
print(workbook_name + " created successfully")
