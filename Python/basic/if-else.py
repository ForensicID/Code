a = 100
b = 10
if b > a:
    print("b lebih besar dari a")
elif a == b:
    print("a dan b sama dengan")
else:
    print("a lebih besar dari b")


c = 20
d = 200
print("A") if c > d else print("B")

e = 1000
f = 1000
print("A") if e > f else print("=") if e == f else print("B")

g = 150
h = 10
i = 1000
if g > h and i > g:
    print("keduanya adalah benar")
