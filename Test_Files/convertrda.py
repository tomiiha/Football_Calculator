import pandas
import feather
path = 'england1939.rda'
datafile = feather.read_dataframe(path)
datafile.to_excel('England Old Data.xlsx')