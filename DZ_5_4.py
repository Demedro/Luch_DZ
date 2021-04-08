def my_func(x, y):
    d = 1
    for i in range(abs(y)):
        d = d / x
    return d


while True:
    try:
        while True:
            x = int(input("введите число: "))
            y = int(input("введите степень: "))
            print(f"Результат: {my_func(x, y)}")
            print()
    except (ZeroDivisionError) as err:
        print(f"Ошибка! Деление на ноль!")
        print()
    except Exception as err:
        print(f"Ошибка! {err}")
        print()
