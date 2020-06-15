import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv', index_col='Country/Region')
print(csv)