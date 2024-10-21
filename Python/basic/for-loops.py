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

# range() Function
for e in range(5):
    print(e)

for f in range(2,5):
    print(f)

for g in range(2, 30, 3):
    print(g)

# Else in For Loop
for h in range(11):
    print(h)
else:
    print("akhirnya")

for i in range(8):
    if i == 3: break
    print(i)
else:
    print("selesai")

# Nested Loops
hewan = ["macan","singa","ular","hiu"]
buah = ["pir","durian","nanas","melon"]

for j in hewan:
    for k in buah:
        print(j,k)

# pass Statement
for l in [0,1,2,3]:
    pass
