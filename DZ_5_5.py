def my_func(a, b, c):
    td = min(a, b, c)
    d = a + b + c - td
    return d


try:
    s = 0
    while True:
        a = input("введите числа: ")
        b = a.split()
        f_b = []
        for x in range(len(b)):
            f_b.append(float(b[x]))
        s = s + sum(f_b)
        print(s)
        print()
except (ValueError) as err:
    s = s + sum(f_b[0:x])
    print(s)
    print(f"Введён спецсимвол")
    print()
except Exception as err:
    print(f"Ошибка! {err}")
    print()
