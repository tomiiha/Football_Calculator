import pandas as pd

# What seasons to include (list off of files)
seasons_included = ["2017-2018","2018-2019"]

# Load excel sheets per seasons_included
for season in seasons_included:
    excel_sheet = pd.read_excel(r'Data\NData' + str(season) + '.xlsx')
    print(excel_sheet)
