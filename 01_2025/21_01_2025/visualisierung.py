# Thema: matplotlib, matplotlib.pyplot und numpy

import os

from scipy import stats

os.environ['TCL_LIBRARY'] = r'C:\Users\Thomas\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Thomas\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

import matplotlib.pyplot as plt
import numpy as np

import tkinter
print(tkinter.TkVersion)

x = np.random.uniform(0.0, 5.0, 250)
plt.hist(x,5)
plt.show()

# Daten Normalverteilung
# Gauß-Daten-Verteilung
# Gauß-Glocke-Verteilung

x = np.random.normal( 5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

# scatter Streuung, Punktdiagramm
# Jeder Punkt braucht zwei Werte
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def m_fun(x):
    return slope * x + intercept

m_model = list(map(m_fun, x))
plt.scatter(x, y)
plt.plot(x, m_model)
plt.show()

print('Steigung: ', slope)
print('Schnittpunkt: ', intercept)
print('Korrelationskoeffizient: ', r)
print('Standard-Fehler: ', std_err)

print('Die Geschwindigkeit eines Wagens, der 10 Jahre als it:' , m_fun(10))