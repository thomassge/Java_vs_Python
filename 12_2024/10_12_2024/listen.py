# Thema: Listen

a = []

if len(a) == 0:
    print("Die Liste ist leer.")
else:
    print("Die Liste hat Elemente.")

if a:
    print(a)
    print(bool(a))

a.append(4)
if a:
    print(a)
    print(bool(a))

b = [1, 2, 3, 'a', 'b']

c = b*2
print(c)

b = [1, 2, 3]
c = b + [2]

print()
