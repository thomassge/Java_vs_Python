import sys

print(sys.version)

if 5>2:
    print("Five is greater than two")

_x = 4

print(_x)

x, y, z = "orange", "red", "blue"
print(x,y,z)

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x, y, z)


x = "awesome"

def myfunc():
    global x
    x = "shit"
    print("Pyth is", x)

myfunc()

print("Pyth is", x)

x = 5
print(type(x))


x = ["apple", "banana", "cherry"]
print(x, type(x))

x = ("apple", "banana", "cherry")
print(x, type(x))

x = {"apple", "banana", "cherry"}
print(x, type(x))

x = {"Fruit": "apple", "Essen":  "banana", "Frucht":  "cherry"}
print(x, type(x))

x = tuple(("apple", "banana", "cherry"))
print(x, type(x))

x = dict(name= "Thomas", age= 26)
print(x)

x = """ Hi
hier gehts weiter
und weiter
"""
print(x)

for x in "banana":
    print(x)
x = "banana"
print(len(x))