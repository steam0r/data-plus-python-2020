import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
print(date[['Province/State', '5/23/20']])