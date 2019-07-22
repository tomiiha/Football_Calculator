import pandas as pd

# What seasons to include (list off of files)
season_list = ["2017-2018","2018-2019"]
excl_value = 10

# Lists
header_list = []

# Create series based on file set
sports_data = [pd.read_excel(r'Data\NData' + str(season) + '.xlsx') for season in season_list]
for i, season in enumerate(season_list):
    sports_data[i]['season'] = season
sports_data = pd.concat(sports_data)
sports_data = sports_data.fillna(value = 0)
sports_data = sports_data[sports_data.games >= excl_value].groupby('season').mean().T
sports_data = round(sports_data,3)
print(sports_data)
