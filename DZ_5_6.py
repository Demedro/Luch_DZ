def int_func(a):
    b = a.capitalize()
    return b


while True:
    try:
        while True:
            a = input("введите текст: ")
            b = a.split()
            c=[]
            for x in b:
                c.append(int_func(x))
            print(' '.join(c))
            print()
    except Exception as err:
        print(f"Ошибка! {err}")
        print()
