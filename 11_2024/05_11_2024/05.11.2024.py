def volumen(a, b, /, c=1):
    v = a * b * c
    return v

def string_neben(a,/,b1="",c1=""):
    v= a+b+c
    return v

a = (input("Geben Sie die Abstände a, b, c ein!"))
b = (input())
c = (input())

print(string_neben(a, b1=b, c1=c))
print(string_neben(a, c1=c, b1=b))

a=int(a)
b=int(b)
c=int(c)

print(volumen(a, b, c))
print(volumen(a, b))
