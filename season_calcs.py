import pandas as pd
import glob, os

# What seasons to include (list off of files)
season_list = []
os.chdir(r"C:\Users\tihalainen\Desktop\Data Stuff")
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
sports_data = sports_data[sports_data.games >= excl_value].groupby('season').mean().T
sports_data = round(sports_data,3)

# Create Excel sheet with dataframe
sports_data.to_excel(r'Summary\Summary NorthamptonTown.xlsx')
print("Summary Created")
