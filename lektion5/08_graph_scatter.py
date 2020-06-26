import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
x = csv['Lat']
y = csv['5/23/20']

plt.scatter(x, y)
plt.show()
