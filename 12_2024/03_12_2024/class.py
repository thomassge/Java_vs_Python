#Thema: Klassen

class Person:
    def __init__(self, name, honorar):
        self.name = name
        self.honorar = honorar

    def __str__(self):
        return f"{self.name} bekommt {self.honorar} Euro."

    def __add__(self, p2):
        return self.honorar + p2.honorar

    def __sub__(self, p2):
        return self.honorar - p2.honorar

    def __mul__(self, other):
        return self.honorar * other.honorar

    def __truediv__(self, other):
        return self.honorar / other.honorar

#if __name__ == '__main__':
print("Du bist in ")

v_name1 = Person("Hans", 1000)
v_name2 = Person("Heinrich", 1300)
v_name3 = Person("Peter", 1500)
v_name4 = Person("Werner", 1700)

print(v_name1 + v_name2)
print(v_name1 - v_name2)
print(v_name1 * v_name2)
print(v_name1 / v_name2)

print((v_name1 + v_name2) + (v_name3 + v_name4))

print(v_name1, v_name2, sep="\n")

