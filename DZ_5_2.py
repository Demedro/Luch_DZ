def delen(a, b):
    d = a / b
    return d


while True:
    try:
        while True:
            fn = int(input("введите делимое: "))
            sn = int(input("введите делимое: "))
            print(f"Результат: {delen(fn, sn)}")
            print()
    except (ZeroDivisionError) as err:
        print(f"Ошибка! Деление на ноль!")
        print()
    except Exception as err:
        print(f"Ошибка! {err}")
        print()
