import random

n = 10
x = []
for i in range(n):
    x.append(random.randint(1, 100))

l = [x[k] for k in range(1, n) if x[k] > x[k - 1]]

print(x)
print(l)
