# Thema: GUI, tkinter

import tkinter as t

# from tkinter import *
f = t.Tk()
f.geometry("300x300")
f.title("Mein erstes Fenster")

l1 = t.Label(f, text="Hallo Welt", font=("Arial", 20))
l1.pack()
l1.grid
