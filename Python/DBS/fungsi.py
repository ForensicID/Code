def minimal(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a

print(minimal(3, 4))
print(minimal(5, 2))
print(minimal(7, 7))