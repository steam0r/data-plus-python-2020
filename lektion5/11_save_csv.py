import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
sorted = date.sort_values(by=['5/23/20'], ascending=False)
data = sorted[['Country/Region', 'Province/State', '5/23/20']].head(10)
data.to_csv('top10.csv', index=False) 