import random

a = []
c = int(input('введите размер выборки '))
for r in range(c):
    a.append(random.randint(1, 100))
print(a)
a.sort()
b = int(input('введите число '))
it = c
while it > 1:
    n = round(it / 2)
    if b < a[n]:
        ans = a[n]
        a = a[:n]
        it = len(a)
    elif b > a[n]:
        ans = a[n]
        a = a[n:]
        it = len(a)
    else:
        ans = a[n]
        break
print(ans)
