'''

#Erstellen leerer Ojekte
liste1 = []
tupel1 = ()
menge1 = {}
dic1 = {}

print(type(liste1))
print(type(tupel1))
print(type(menge1))
print(type(dic1))


#Erstellen leerer Ojekte mit Cast-Funktionen
liste2 = list([])
tupel2 = tuple()
menge2 = set({})
dic2 = dict({})

print(type(liste2))
print(type(tupel2))
print(type(menge2))
print(type(dic2))


#Erstellen leerer Ojekte mit Elementen
liste2 = list[1, 2.0, 3+5j, True, "False", liste1]
print("liste2 = ", type(liste2))

tupel = ("a")
print("tupel = ", type(tupel))
tupel0 = ("a",)
print("tupel0 = ", type(tupel0))

tupel2 = 1, 2.0, 3+5j, True, "False", liste1
print("tupel2 = ", type(tupel2))
tupel3 = (1, 2.0, 3+5j, True, "False", liste1)
print("tupel3 = ", type(tupel3))

menge2 = {1, 2.0, 3+5j, True, "False", 1.0, 0, 0.0}
print("menge2 = ", type(menge2))
dic2 = {1: 2.0, 3+5j: True, "False":liste1}
print("dic2 = ", type(dic2))
'''


#Elemente einfügen
liste1 = []

liste1.append("1.Element")
print(liste1)

liste1.insert(0, "2.Element")
print(liste1)

liste1.append("3.Element")
print(liste1)

liste3=liste1

liste5 = liste1 copy()
liste6 = liste1.copy()
