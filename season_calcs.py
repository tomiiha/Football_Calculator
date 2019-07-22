import pandas as pd

# What seasons to include (list off of files)
season = "2018-2019"
season_list = ["2017-2018","2018-2019"]

# Lists
header_list = []

# Load excel sheets per seasons_included - no data to 0
for seas in season_list:
    excel_sheet = pd.read_excel(r'Data\NData' + str(seas) + '.xlsx')
    excel_sheet = excel_sheet.fillna(value = 0)
    
# Load headers from files
    headers = excel_sheet.columns.values.tolist()
    if headers not in header_list:
        header_list.append(headers)
        
# Run calcs on individual headers
    for header in header_list:
        data_mean = excel_sheet[header][excel_sheet.games >= 10].mean()
        data_mean = round(data_mean,2)
        print(data_mean)
