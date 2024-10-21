# For Loops
buwah = ["apel","anggur","melon"]
for x in buwah:
    print(x)

buwah = ["apel","anggur","melon"]
for b in buwah:
    print(b)
    if b == "anggur":
        break

# break Statement
for c in buwah:
    if c == "anggur":
        break
    print(c)

# continue Statement
for d in buwah:
    if d == "melon":
        continue
    print(d)
