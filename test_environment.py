to_parse = ["player","position","age"]
grab_start = to_parse[0]
for data_point in to_parse:
	findinfo = parsepage.find_all('td',attrs={"data-stat":data_point})
	for datum in findinfo:
		add_datum = datum.get_text()
		if add_datum != 'coverage note':
			sotlist.append(addsot)
