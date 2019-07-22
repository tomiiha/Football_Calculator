import pandas as pd

# What seasons to include (list off of files)
season = "2018-2019"

# Lists
header_list = []

# Load excel sheets per seasons_included
excel_sheet = pd.read_excel(r'Data\NData' + str(season) + '.xlsx')
headers = excel_sheet.columns.values.tolist()
    if headers not in header_list:
        header_list.append(headers)

# Overview Calcs
for header in header_list:
    data_mean = excel_sheet[header].mean()
    data_median = excel_sheet[header].median()
    print(round(data_mean,2))
