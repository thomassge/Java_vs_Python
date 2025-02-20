'''
def funktion_nr1():
    print("Das ist Funktion Nummer 1!")

def funktion_nr2():
    print("Das ist Funkton Nr. 2!")

def funktion_nr3():
    print("Das ist Funktion Nr. 3!")

while True:
    print("Wähle Funktion 1, 2, oder 3 aus: ")

    auswahl = input("Welche wählst du: ")

    match auswahl:
        case '1': funktion_nr1()
        case '2': funktion_nr2()
        case '3': funktion_nr3()
        case _: break



Neue Aufgabe


def celToFahr():
    value = float(input("Bitte gib eine Temperatur ein: "))
    value = (value*1.8) + 32
    print("Neuer Wert in Fahrenheit: " , value)

def fahrToCel():
    value = float(input("Bitte gib eine Temperatur ein: "))
    value = (value / 1.8) - 32
    print("Neuer Wert in Fahrenheit: " , value)

def celToKel():
    value = float(input("Bitte gib eine Temperatur ein: "))
    value = value + 273.15
    print("Neuer Wert in Fahrenheit: " , value)

while True:
    print("Celsius in Fahrenheit - 1")
    print("Fahrenheit in Celsius - 2")
    print("Celsius in Kelvin - 3")

    calculation = input("1, 2 oder 3:")

    match calculation:
        case '1':
            celToFahr()
        case '2':
            fahrToCel()
        case '3':
            celToKel()

        case _:
            break
print("Ende")


'''
"Neue Aufgabe"

shoppingList = []

def addItem():
    shoppingList.append(input("Bitte gib ein Lebensmittel ein: "))

def removeItem():
    shoppingList.remove(input("Bitte gib das Lebensmittel ein dass du entfernen möchtest: "))

def printShoppingList():
    print(shoppingList)

while True:
    print("Lebensmittel hinzufügen: 1")
    print("Lebensmittel entfernen: 2")
    print("Shoppinglist anzeigen: 3")

    auswahl = input("1, 2, 3: ")

    match auswahl:
        case '1':
            addItem()
        case '2':
            removeItem()
        case '3':
            printShoppingList()
        case _:
            break
print("-_-_- ENDE -_-_-")