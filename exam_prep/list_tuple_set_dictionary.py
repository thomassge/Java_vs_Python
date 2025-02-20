'''
Listen: Erstellen, hinzufügen, löschen, (erweitern)
'''

"""Erstellen"""
mylist = ["apple", "banana", "cherry", "apple"]
print(mylist, len(mylist))

mycraplist = ["apple", 3, True]
print(mycraplist, len(mycraplist), type(mycraplist))

mymorecraplist = list(("apple", "banana", "cherry"))
print(mymorecraplist, type(mymorecraplist))

print(mylist[0])


"""Hinzufügen"""
mylist[1] = "pineapple"
print(mylist[2])

mylist.insert(4, "watermelon")
print(mylist)

mylist.append("pie")
print(mylist)


"""Löschen"""
mylist.remove("apple")
print(mylist)

mylist.pop(0)
print(mylist)


del mylist[0]
print(mylist)

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

i=0
while i<len(mylist):
    print(mylist[i])
    i = i+1

'''
Tuple
'''

thistupel = ("apple", "banana", "cherry", "apple")
print(thistupel, len(thistupel))

thistupel = ("apple", )
print(thistupel)

thistupel = tuple(("apple", "banana", "cherry"))
print(thistupel, type(thistupel))


"""
Ändern:
erst in Liste umwandeln,
bearbeiten und wieder als tuple speichern
"""

thistupel = ("apple", "banana", "cherry")
y = list(thistupel)
y[1] = "kiwi"
thistupel = tuple(y)
print(thistupel)

thistupel = ("apple", "banana", "cherry")
y = list(thistupel)
y.append("watermelon")
thistupel = tuple(y)
print(thistupel)

thistupel = ("apple", "babana", "cherry")
y = list(thistupel)
y.insert(1, "kiwi")
thistupel = tuple(y)
print(thistupel)

"""
Löschen:
erst in Liste umwandeln,
bearbeiten und wieder als tuple speichern
"""
y = list(thistupel)
y.remove("kiwi")
thistupel = tuple(y)
print(thistupel)

y = list(thistupel)
del y


'''Sets'''

thisset = {"apple", "banana", "cherry", 'apple'}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset, len(thisset), type(thisset))

thisset = set(("apple", "banana", "cherry", True, 1, 2))
print(thisset)

"""Access"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

"""Hinzufügen"""
thisset = {"apple", "banana", "cherry"}
thisset.add("kiwi")
print(thisset)


tropical = {"Gurke", "Karotte", "Ananas"}
thisset.update(tropical)
print(thisset)

jay = ["natz"]
thisset.update(jay)
print(thisset)

"""Löschen"""
thisset.remove("natz")
print(thisset)

## discard prüft nicht
thisset.discard("Gurke")
print(thisset)

## pop löscht random
thisset.pop()
print(thisset)

## del löscht ganz set
del thisset


'''Dictionaries'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "location": list(("GER", "US", "GR"))
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

thisdict = dict(name = "Thomas",
                age = 26,
                location  = "Frankfurt")
print(thisdict)

"""Access"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x)

x = thisdict.get("year")
print(x)

x = thisdict.keys()
print(x)

thisdict["color"] = "white"
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

thisdict["year"] = 2020
print(x)


"""Ändern"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2020
print(thisdict)

thisdict.update({"brand": "Benz"})
print(thisdict)

"""Löschen"""
thisdict.pop("model")
print(thisdict)

## löscht das zuletzt hinzugefügte item
thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

del thisdict

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = [1999, 2020]
print(thisdict)

newdic = dict(brand= ("BMW", "Mercedes","Audi"),
              model = "S-Klasse",
              year = 2024)
print(newdic)

newdic = thisdict.copy()
print(newdic)
