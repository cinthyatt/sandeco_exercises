from random import randint
vector = []
for i in range (10):
    x = randint(1, 100)
    vector.append(x)

print(vector)
print(sum(vector))
print(sorted(vector))
