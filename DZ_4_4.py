r = [7, 5, 3, 3, 2]
try:
    while True:
        mon = int(input("введите число: "))
        # r.append(mon)
        # r.sort(reverse=True)
        # print(r)
        for i in range(len(r))[::-1]:
            if mon <= r[i]:
                r.insert(i + 1, mon)
                break
            elif i == 0:
                r.insert(0, mon)
        print(r)
except Exception as err:
    print(f"Ошибка! {err}")
