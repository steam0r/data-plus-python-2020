import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
sorted = date.sort_values(by=['5/23/20'], ascending=False)
print(sorted[['Country/Region', 'Province/State', '5/23/20']].head(10))