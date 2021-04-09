l = (k for k in range(100, 1001) if k % 2 == 0)
a = 1
for x in l:
    a = a * x

print(a)
