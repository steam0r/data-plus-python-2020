import math
import matplotlib.pyplot as plt

daten = range(10)
plt.figure(figsize=(10,10))
plt.xlabel("Alle X", fontsize=20)
plt.ylabel("Alle Y", fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(daten, [math.pow(x, 2) for x in daten], color="red", linewidth=3)
plt.show()