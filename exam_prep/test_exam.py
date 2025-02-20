from cProfile import label

x = 5

def outer():
    x = 10
    def inner():
        global x
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)


#1 x=6
#2 x=10
#3 x=6

""""""

import pickle

data = {'Name': 'Alice', 'Alter': 25}
with open('test.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)

# mit pickle.dump schreiben wir das dict 'data' in die datei 'test.pkl'
# das 'wb' steht für write byte, das das schreiben in eine DAtei ebenfalls verdeutlicht

# mit pickle.load lesen wir  die 'test.pkl' datei, was durch das 'rb' -> read byte
# ebenfalls unterstrichen wird

# ausgabe:  {'Name': 'Alice',
#           'Alter': 25 }

""""""

# mean(): berechnet den durchschnitt
# median(): sortiert eine Liste und zeigt auf den mittleren Wert dieser Liste
# std(): berechnet die Standardabweichung zwischen den Werten
# uniform(): generiert zufallszahlen gleichmäßig im gegebenen Bereich
# hist(): Zeichnet ein Histogram bzw, ein Balkendiagram von eingegebenen Werten
# show(): Zeigt das Histogram beispielsweise

""""""

# linregress(): Berechnet die Verteilung von x und y Werten

# scatter(): berechnet ein Punktdiagramm
# plot(): zeichnet eine Linie
# matplotlib: ist eine Bibliothek fpr das ERstellen für Diagrammen

""""""

# match-case:   beschreibt ein Programmierverfahren, das auf versch. Ereignisse
#               reagiert, wie bspw. Benutzeriengaben und dadurch Aktionen ausgelöst werden,
#               wie zb Funktionsaufrufe

""""""

print(list(range(2, 10, 2)))
# printed eine Liste beginnend mit Index [2] bis Index [10] in zweier Schritten
# range(): Die erste Zahl steht für den Startindex, die zweite für End-Bedingung
#           und die dritte für die Sprünge

""""""

import tkinter as tk
f = tk.Tk()
f.geometry("400x500+10+50")
f.title("Test_Chat_GPT")

def close():
    f.destroy()

def printText():
    label1 = tk.Label(f, text = "Hallo, Tkinter!")
    label1.grid(row = 2, column = 0)

button1 = tk.Button(f, text = "Klick mich", command = printText)
button1.grid(row = 1, column = 0)

button2  = tk.Button(f, text  = "Exit", command = close)

f.mainloop()

""""""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

x = np.random.uniform(0.0, 5.0, 50)

plt.hist(x)
plt.show()


# b)
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, r_value, p_value, intercept, std_err = linregress(x, y)

plt.scatter(x,y)
plt.plot(x, [slope * xi + intercept for xi in x])

plt.show()

""""""

print("Montag - 1")
print("Dienstag - 2")
print("Mittwoch - 3")
print("Donnerstag - 4")
print("Freitag - 5")
print("Samstag - 6")
print("Sonntag - 7")

def wochentag_name(n):


    match n:
        case '1':
           return "Montag"
        case'2':
            return "Montag"



""""""
""""""
""""""

# Aufgabe 1:
# pickle.dump(obj, file): schreibt Objekte in eine Datei rein
# global, nonlocal: globale Variable schreibt man ganz links und sie gelten in allen Methoden
#                    nonlocal Variable gelten innerhalb Funktionen
# range(start, stop, step): beschreibt die Länge einer for-Schleife,
                            #startpunkt, endpunkt, sprünge
# tkinter.Label(): erstellt ein Label für GUI
# random.uniform(a, b): erstellen eine gleichverteilte Zahlenreihe zw. a und b
# numpy.mean(): berechnet den durchschnitt
# matplotlib.hist(): erzeugt ein Histgram bzw. balkendiagramm
# str(): String-Konstruktor
# match-case: programmiermethoden um bspw. aus user eingaben funktionsaufrufe zu generieren
# input(): speichert eine Benutzereingabe

# Aufgabe2:
x = 10

def outer():
    x = 5
    def inner():
        global x
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
# Ausagbe: 11, 5, 11 -> erst global, dann non-local, dann wieder global

import random
numbers = [random.randint(1, 10) for _ in range(5)]
print(numbers)
print(sorted(numbers))
# Ausgabe: hier werden 5 random Zahlen zwischen 1-10 generiert

data = {'Name': 'Max', 'Alter': 30}
with open('test.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data['Name'])
# pickle.dump schreibt 'data' ins Dokument 'test.pkl'
# pickle.load schreibt liest die daten aus den dokument und speicher
# sie in loaded_data
# print: "'Name': 'Max'"


# Aufgabe 3
def main():
    while True:
        print("Wähle zwischen 1, 2, 3")
        eingabe = int(input())

        match eingabe:
            case 1:
                eingeben()
            case 2:
                ausgeben()
            case 3:
                break
main()

bauern = []
def eingeben():
        name = input("Bitte Name eingeben")
        laenge = float(input("Länge"))
        breite = float(input("Breite"))
        bauern.append({'Name': name, 'Länge': laenge, 'Breite': breite})

def flaeche(bauer):
    return bauer['Länge'] * bauern['Breite']

def steuer(bauer):
    return flaeche(bauer) * 0.1

def ausgeben():
    for bauer in bauern:
        print(f"{bauer['Name']} - Fläche: {flaeche(bauer)} m2 - Steuern: {steuer(bauer)}€")
def close():
    return 0

# Aufgabe 4
import tkinter as tk
f = tk.Tk()
f.geometry("400x500+50+100")
f.title("Python-Informatik")

def saave():
    z1 = entry1.get()
    label3 = tk.Label(f, text = "Ihre Wunschnote: " + str(z1))
    label3.grid(row = 2, column = 1)

def close():
    f.destroy()

label1 = tk.Label(f, text = "Heute: 20.02.2025 - Pythen-Informatik")
label1.grid(row = 0,  column = 0)

label2 = tk.Label(f, text = "Geben Sie Ihre Wunschpte ein!")
label2.grid(row = 1, column = 0)
entry1 = tk.Entry()
entry1.grid(row = 1, column = 1)

button1 = tk.Button(f,  text = "Eingeben", command = saave)
button1.grid(row = 3, column = 1)

button2 = tk.Button(f, text = "Beenden", command=close)
button2.grid(row = 4, column = 1)

f.mainloop()

# Aufgabe 5
def geburtsdatum():
    gebdat = input("Gib dein Geburtsdatum ein (TT.MM.JJJJ): ")
    return gebdat
# Fehler: "Gib dein Geburtsdatum ein (TT.MM.JJJJ): " sollte eine Zeile weiter oben stehen in einem print stehen
#           input sollte leer bleiben und von einen String-Konstruktor umschlossen

def jahr(datum)
    jahr = datum[6:10]
    return jahrZ
# Fehler: ':' fehlt
#          Rückgabe variabe muss jahr heißen

def alter(jahrZahl):
    alterHeute = 2024 - jahrZahl
    return
# Fehler: keine Return Variable, da muss alterHeute rein

print("1." + a == b)
# Fehler: zuweisungsoperator ungultig in print statement

for i in range[5]:
    print(i)
# Fehler: runde statt eckige Klammern in range

a = "info"
for i in range(len(a)):
    print(a(i))
# Fehler: a ist keine Liste, sie hat zwar eine länge (4) aber man kann nicht
#           i-mal durch iterrieren

liste = [ ]
liste.pop()
# Fehler: Liste ist schon leer, nichts zu poppen

def flaeche(l, b=None):
    if b = None:
        print(f"Die Quadratfläche beträgt: {l*l}")
# Fehler: b ist immer None