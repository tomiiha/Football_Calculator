from bs4 import BeautifulSoup as bsoup
import requests as reqs
page_to_parse = 'https://fbref.com/en/squads/986a26c1/Northampton-Town'
page = reqs.get(page_to_parse)
parse_page = bsoup(page.content, 'html.parser')
position_list = []
age_list = []

# Need to somehow get the 'sotlist' variable to change when the data_point changes
# Add +1 to grab start to shift the list
to_parse = ["position","age"]
grab_start = 0
parse_start = to_parse[grab_start]
for data_point in to_parse:
	findinfo = parse_page.find_all('td',attrs={"data-stat":data_point})
	for datum in findinfo:
		add_datum = datum.get_text()
		if add_datum != 'coverage note':
			position_list.append(add_datum)
			
print(position_list)
print(age_list)
