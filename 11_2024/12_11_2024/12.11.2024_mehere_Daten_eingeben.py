#Thema: mehrere Daten mit einem Enter eingeben
#eval()

liste0 = eval(input("Gib Elemente einer Liste an!"))
print("liste0:", type(liste0), liste0)

liste1 = exec(input("Gib Elemente einer Liste an!"))
print("liste1:", type(liste1), liste1)

prog = "a=2\nb=5\nc=pow(a,b)\nprint(c)"
#prog = input()
print(prog)
exec(prog)