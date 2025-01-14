# Thema: Maschinelles Lernen
from statistics import median

import numpy as np
# mean(), median(), mode()
import scipy.stats as stats

liste1 = [99,86,87,88,111,86,103,87,77,85,86]

mean = np.mean(liste1)
print("mean:", mean)

median = np.median(liste1)
print("meadian: ", median)

liste2 = liste1.copy()
liste2.pop(4)
x2 = np.median(liste2)
print("median von liste2: ", x2)

x3 = stats.mode(liste1)
print("Häufigkstewert: ", x3)

# Standardabweichung
x4 = np.std(liste1)
print("Standardabweichung: ", x4)

#4 Variance
x5 = np.var(liste1)
print("Variance: ", x5)
print(x5**0.5)

#5 Percentile
liste5 = [5, 31, 43, 48, 50, 42, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x8 = np.percentile(liste5, 25)
x9 = np.percentile(liste5, 50)
x7 = np.percentile(liste5, 75)

print("25. Percentile: ", x8)
print("50. Percentile: ", x9)
print("75. Percentile: ", x7)

x10 = np.median(liste5)
print("Median: ", x10)



