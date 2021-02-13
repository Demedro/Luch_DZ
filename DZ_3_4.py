s = {"1", 5, 7, "2", (5, 9), "6"}
s1 = []
s2 = []
ct = 0
while True:
    if ct == 0:
        for x in s:
            s1.append(x)
    else:
        s2=[]
        for x in s:
            s2.append(x)
        if s1 != s2:
            break
    ct += 1

print(ct)
