import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
csv.plot()
plt.savefig("covid19.png")
