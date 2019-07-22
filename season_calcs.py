import pandas as pd

# What seasons to include (list off of files)
season_list = ["2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010","2010-2011", "2011-2012","2012-2013","2013-2014","2014-2015","2015-2016","2016-2017","2017-2018","2018-2019"]
excl_value = 5

# Create series based on file set
sports_data = [pd.read_excel(r'Data\NData' + str(season) + '.xlsx') for season in season_list]
for i, season in enumerate(season_list):
    sports_data[i]['season'] = season
sports_data = pd.concat(sports_data)
sports_data = sports_data.fillna(value = 0)
sports_data = sports_data[sports_data.games >= excl_value].groupby('season').mean().T
sports_data = round(sports_data,3)

# Create Excel sheet with dataframe
sports_data.to_excel(r'Data\NData BD.xlsx')
