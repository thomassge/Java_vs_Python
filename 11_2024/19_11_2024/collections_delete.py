#Einfügen

liste0 = [1, 2, 3, 4, 5]
print(liste0)
liste0.append(6)
print(liste0)
liste0.insert(1,10)
print(liste0)


tuple0 = (1, 2, 3, 4, 5)
print(tuple0)
tuple0= tuple0 + (6,)
print(tuple0)

liste1 = list(tuple0)
liste1.insert(3, "liste")
print(type(liste1), liste1)

tuple0 = tuple(liste1)
print(type(tuple0), tuple0)

liste2 = liste1
liste2 = liste1.copy()

menge0 = set(liste0)
print(type(menge0), menge0)
menge0.add(10)
print(menge0)

dic0 = dict(a=1, b=2, c=3)
print("dic0: ", type(dic0), dic0)
print("menge0: ", type(menge0), menge0)

#Elemente ablesen

print(liste0.index(2))
print(dic0['b'])
print(dic0.get('b'))

#Anzahl der Elemente in den Collections
print("Anzahl der Elemente in liste0: ", len(liste0))
print("Anzahl der Elemente in tuple0: ", len(tuple0))
print("Anzahl der Elemente in dic0: ", len(dic0))
print("Anzahl der Elemente in menge0: ", len(menge0))

print(menge0)
menge0.add(False)
menge0.add(0.0)
menge0.add(True)
menge0.add(1.0)
print("Anzahl der Elemente in menge0: ", len(menge0))
print(menge0)

#Löschen
print("liste0: ", liste0)
print("Das letzte Element in der Liste", liste0.pop())
print("liste0: ", liste0)

try:
    print(liste0.remove(2))
    print("liste0: ", liste0)
except:
    print("Das Element ist nicht in der Liste")
liste3=["a","b","c"]
print(liste3)






