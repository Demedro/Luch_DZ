def my_func(a, b, c):
    td = min(a, b, c)
    d = a + b + c - td
    return d


while True:
    try:
        while True:
            a = int(input("введите первое число: "))
            b = int(input("введите второе число: "))
            c = int(input("введите третье число: "))
            print(f"Результат: {my_func(a, b, c)}")
            print()
    except Exception as err:
        print(f"Ошибка! {err}")
        print()
