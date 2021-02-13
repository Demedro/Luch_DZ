try:
    while True:
        t = int(input('введите число: '))
        c = 0
        while not((t > 0) and (t < 1)):
            t = t / 10
            c += 1
        print(c)
except Exception as err:
    print (f"Ошибка! {err}")


