#Thema: global, globals(), nonlocal

def f1():
    global v0
    v0 = 10
    print("in f1 v0 = ", v0)
f1()
print("v0 ist in der globalen Ebene: ", v0)

def f2():
    print(v0*20)
f2()

def f3():
    global v1, v2
    v1 = 10
    v2 = 20
    print("in f1 v1 = ", v1)
    print("in f1 v2 = ", v2)
f3()
print("v1 und v2 sind global", v1, v2)

def f4():
    global v1, v2
    v1 = 30
    v2 = 40
    print("in f4 v1 = ", v1)
    print("in f4 v2 = ", v2)
f4()
print("v1 und v2 sind global", v1, v2)


# globals() ist ein eingebautes Python-Modul, das ein Dictionary aller globalen Variablen in einem Skript zurückgibt.
d = globals().copy()

# items(), keys(), values()
#print(globals().keys())

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)

for i  in enumerate(d.items(), start= 1):
    print(i)