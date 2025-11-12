
#pares = {2, 4}
pares = set()
for n in range(2,21):
    if n % 2 == 0:
        pares.add(n)
print(pares)

#tres = {3, 6}
tres = set()
for n in range(3, 31):
    if n % 3 == 0:
        tres.add(n)
print(tres)

uniao = pares.union(tres)
print(uniao)

intersec = pares.intersection(tres)
print(intersec)

dif1 = pares.difference(tres)
dif2 = tres.difference(pares)
dif = dif1.union(dif2)
print(dif)