import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
data = csv[['Long', 'Lat']]

ruh_m = plt.imread('welt.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(csv['Long'], csv['Lat'], zorder=1, alpha= 0.2, c='b', s=10)

box = (-180, +180, -90, 90)

ax.set_title('COVID-19 recoveries all over the worlds')
ax.imshow(ruh_m, zorder=0, extent = box, aspect= 'equal')
plt.show()