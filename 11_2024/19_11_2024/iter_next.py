#Thema iter() und next()

liste1 = ["a", "b", "c", "d"]
iter_a = iter(liste1)

try:
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))
except:
    print("Keine Iteration mehr")

a = liste1.__iter__()
print(a.__next__())