import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv[['Lat', 'Long', '5/23/20']])