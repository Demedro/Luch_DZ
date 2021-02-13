s = []
while True:
    t = input("введите элемент списка: ")
    if t == 'end':
        break
    else:
        s.append(t)
print(s)

for i in range(0, len(s), 2):
    if i < len(s)-1:
        s[i], s[i + 1] = s[i + 1], s[i]
print(s)
