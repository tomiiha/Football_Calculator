# Calculation legend: # Goals (G), Assists (A), Penalties (PK), Shots on Target (SOT), Fouls (F), Cards (C)
import pandas as pd
import glob, os

# What seasons to include (list off of files)
season_list = []
curr_fold = os.getcwd()
os.chdir(curr_fold)
for file in glob.glob("*.xlsx"):
    file = file[-14:-5]
    season_list.append(str(file))
    
# Min games played
excl_value = 5

# Create series based on file set
sports_data = [pd.read_excel("Data Northampton Town Season " + str(season) + ".xlsx") for season in season_list]
for i, season in enumerate(season_list):
    sports_data[i]['season'] = season
sports_data = pd.concat(sports_data)
sports_data = sports_data.fillna(value = 0)

# Add Over-90 calculations
sports_data['G/90'] = sports_data['goals'] / (sports_data['minutes'] / 90)
sports_data['A/90'] = sports_data['assists'] / (sports_data['minutes'] / 90)
sports_data['G+A/90'] = (sports_data['goals'] + sports_data['assists']) / (sports_data['minutes'] / 90)
sports_data['G-PK/90'] = (sports_data['goals'] - sports_data['pens_made']) / (sports_data['minutes'] / 90)
sports_data['G+A-PK/90'] = ((sports_data['goals'] - sports_data['pens_made']) + sports_data['assists']) / (sports_data['minutes'] / 90)
sports_data['SOT/90'] = sports_data['shots_on_target']/(sports_data['minutes']/90)
sports_data['F/90'] = sports_data['fouls']/(sports_data['minutes']/90)
sports_data['C/90'] = (sports_data['cards_yellow'] + sports_data['cards_red']) / (sports_data['minutes'] / 90)

# Average calculation on the above calcs and parsed data
sports_data = sports_data[sports_data.games >= excl_value].groupby('season').mean().T
sports_data = round(sports_data,3)

# Create Excel sheet with dataframe
sports_data.to_excel(r'Summary\Summary NorthamptonTown.xlsx')
print("Summary Created")
