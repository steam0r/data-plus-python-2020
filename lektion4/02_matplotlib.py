import math
import matplotlib.pyplot as plt

daten = range(10)
plt.plot(daten, [math.pow(x, 2) for x in daten])
plt.show()