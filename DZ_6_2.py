import random

n = 20
x = []
for i in range(n):
    x.append(random.randint(1, 100))

l = [x[k] for k in range(n) if x.count(x[k]) < 2]

print(x)
print(l)