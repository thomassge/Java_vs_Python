# Aufgabe: Konsolenausgabe ermitteln

# Vorgaben: Nutzung nur von List und Dictionary

# Ausgangsstrukturen:
listA = [10, 20, 30, 40, 50]
dictB = {"x": 99, "y": 88, "z": 77}

# Zugriff über eine zweite Referenz:
listC = listA  # Zeigt auf dieselbe Liste wie listA
dictC = dictB  # Zeigt auf dasselbe Dictionary wie dictB

print(len(listA))
print(len(dictB))

def main_operation():
    global dictB
    localDict = dictB

    def inner():
        nonlocal localDict
        print(len(localDict))


        for i in range(len(listC)):
            try:

                removed = listC.pop(i)
                print(removed)
                print(listA)

                dict_items = list(localDict.items())
                dict_items.pop()
                localDict = dict(dict_items)

                print(len(localDict))
                print(localDict)

            except:
                print("Nichts mehr zu löschen.")
                break

    inner()

main_operation()
