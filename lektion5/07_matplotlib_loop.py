import os
import pandas
import matplotlib.pyplot as plt

os.makedirs('images', exist_ok=True)
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
countries = csv['Country/Region']
for country in countries:
    data = csv[csv['Country/Region'] == country]
    print("plotting " + country + "...")
    data.plot()
    plt.savefig("images/" + country + "_covid19.png")
