import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
country = csv[csv['Country/Region'] == 'Germany']
keys = country.keys()
keys = keys.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
data = country[keys].transpose()
data.plot()
plt.show()
