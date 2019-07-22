import pandas as pd

# What seasons to include (list off of files)
season = "2018-2019"

# Lists
header_list = []

# Load excel sheets per seasons_included
excel_sheet = pd.read_excel(r'Data\NData' + str(season) + '.xlsx')
excel_sheet = excel_sheet.fillna(value = 0)
headers = excel_sheet.columns.values.tolist()
if headers not in header_list:
    header_list.append(headers)

# Overview Calcs
for header in header_list:
    data_mean = excel_sheet[header][excel_sheet.games > 10].mean()
    data_mean = round(data_mean,2)
    data_median = excel_sheet[header][excel_sheet.games > 10].median()
    data_median = round(data_median,2)
    print(data_mean)
