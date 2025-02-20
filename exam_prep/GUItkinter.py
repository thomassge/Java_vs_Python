'''

import tkinter as t
from tkinter.ttk import Label


f = t.Tk()

f.geometry("400x300+200+100")

f.title("Heute ist Dienstag")

def schliessen():
    f.destroy()

def addieren():
    zahl1 = entry1.get()
    zahl2 = entry2.get()
    ergebnis  = float(zahl1) + float(zahl2)

    l_summe = t.Label(f, text = zahl1 + " + " + zahl2 + " = " + str(ergebnis))
    l_summe.grid(row = 3, column = 1)

label0 = t.Label(f, text ="Addieren von zwei Zahlen")
label0.grid(row = 0, column = 0)

# Label und Entry für die erste Zahl
label1 = t.Label(f, text ="1. Zahl eingeben")
label1.grid(row = 1, column = 0)
entry1 = t.Entry(f)
entry1.grid(row= 1, column= 1)

# Label und Entry für die zweite Zahl
label2 = t.Label(f, text ="2. Zahl eingeben")
label2.grid(row = 2, column = 0)
entry2 = t.Entry(f)
entry2.grid(row = 2, column= 1)

# Addieren-Button
add_button = t.Button(f, text = "Addieren", command = addieren)
add_button.grid(row=3, column=0)

# ergebnis-Label
ergebnis_label = t.Label(f, text= "Ergebnis")
ergebnis_label.grid(row = 3, column = 1)

#exit-Button
exit_button = t.Button(f, text = "Exit", command = schliessen)
exit_button.grid(row = 4, column = 0)

f.mainloop()





import tkinter as tk

f = tk.Tk()

f.title("Heute ist Montag")

def subtrahieren():
    z1 = entry1.get()
    z2 = entry2.get()

    ergebnis = float(z1) - float(z2)
    ergebnis_sub = Label(f, text = z1 + " - " + z2 + " = " +str(ergebnis) )
    ergebnis_sub.grid(row = 3, column = 1)

def close():
    f.destroy()

label0 = tk.Label(f, text = "Subtrahieren zweier Zahlen")
label0.grid(row = 0, column = 0)

label1 = tk.Label(f, text = "1. Zahl eingeben")
label1.grid(row = 1, column = 0)
entry1 = tk.Entry()
entry1.grid(row = 1, column = 1)

label2 = tk.Label(f, text = "2. Zahl eingeben")
label2.grid(row = 2, column = 0)
entry2 = tk.Entry()
entry2.grid(row = 2, column = 1)

sub_button = tk.Button(f, text = "Subtrahieren", command = subtrahieren)
sub_button.grid(row = 3, column = 0)

exit_button = tk. Button(f, text = "Exit" , command = close)
exit_button.grid(row = 4, column = 1)

f.mainloop()

from tkinter import Label

"""NEUE AUFGABE"""
import tkinter as tk

f = tk.Tk()
f.title("Heute ist Mittwoch!")

def mult():
    z1 = entry1.get()
    z2 = entry2.get()

    ergebnis = float(z1) * float(z2)

    label3 = tk.Label(f, text = "Ergebnis: " + str(ergebnis))
    label3.grid(row = 4, column = 1)

def finish():
    f.destroy()

label0 = tk.Label(f, text = "Multiplizieren von zwei Zahlen")
label0.grid(row = 0, column = 0)

label1 = tk.Label(f, text = "1. Zahl eingeben")
label1.grid(row = 1, column = 0)
entry1 = tk.Entry()
entry1.grid(row = 1, column = 1)

label2 = tk.Label(f, text = "2. Zahl eingeben")
label2.grid(row = 2, column = 0)
entry2 = tk.Entry()
entry2.grid(row = 2, column = 1)

button0 = tk.Button(f, text = "Multiplizieren", command = mult)
button0.grid(row = 3, column = 0)

button1 = tk.Button(f, text = "Schließen", command = finish)
button1.grid(row = 4, column = 0)

f.mainloop()


import tkinter as tk
from tkinter import mainloop
from tkinter.ttk import Label

f = tk.Tk()
f.title = "Heute ist Mittwoch"

def div():
    z1 = entry1.get()
    z2 = entry2.get()

    ergebnis = float(z1) / float(z2)

    label0 = tk.Label(f, text = "Ergebnis: " + str(ergebnis))
    label0.grid(row = 3, column = 1)

def close():
    f.destroy()

label1 = tk.Label(f, text = "Dividieren von zwei Zahlen")
label1.grid(row = 0, column = 0)

label2 = tk.Label(f, text = "1. Zahl eingeben")
label2.grid(row = 1, column = 0)
entry1 = tk.Entry()
entry1.grid(row = 1, column = 1)

label3 = tk.Label(f, text = "2. Zahl eingeben")
label3.grid(row = 2, column = 0)
entry2 = tk.Entry()
entry2.grid(row = 2, column = 1)

button0 = tk.Button(f, text = "Multiplizieren", command = div)
button0.grid(row = 3, column = 0)

button1 = tk.Button(f, text = "Exit", command = close)
button1.grid(row = 4, column = 0)

f.mainloop()
'''

'''Neue Aufgabe'''

import tkinter as tk

f  = tk.Tk()
f.geometry("400x500+50+100")
f.title("Mein-Tkinter-Fenster")

def close():
    f.destroy()

def anzeigenFunktionen():

    benutzerEingabe = entry1.get()

    label3.config(text = "Eingegebener Text: " + benutzerEingabe)


label1 = tk.Label(f, text = "Heute ist der 25.02.2025 - Herzlich Willkommen!")
label1.grid(row = 0, column = 0)

label2 = tk.Label(f, text = "Bitte geben Sie einen beliebigen Text ein: ")
label2.grid(row = 1, column = 0)
entry1 = tk.Entry(f)
entry1.grid(row = 1, column = 1)

label3 = tk.Label(f, text = "Hier wird ihr Text angezeigt")
label3.grid(row = 4, column = 1)

button1 = tk.Button(f, text = "Anzeigen", command = anzeigenFunktionen)
button1.grid(row = 2, column = 1)

button2 = tk.Button(f, text = "Beenden", command = close)
button2.grid(row = 3, column = 1)

f.mainloop()