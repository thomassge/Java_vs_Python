import matplotlib.pyplot as plt
import numpy as np
'''
#x = np.random.uniform(0.0, 5, 2500)
x = np.random.normal(5, 1, 100000)

plt.hist(x, 100)
plt.show()


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

from scipy import stats
slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept
myModel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()
'''


"""Neue Aufgabe"""
from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,5,6,9,8])
y = np.array([8,9,8,87,4,2])

# Lineare Regression berechnen
slope, intercept, r_value, p_value, std_err = linregress(x,y)

# Regressionsgerade berechnen
y_pred = slope * x + intercept

# Streudiagramm
plt.scatter(x, y)

# Regressionsgerade zeichnen
plt.plot(x, y_pred)

plt.show()