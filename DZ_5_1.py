try:
    i = 0
    t = ()
    t1 = []
    d = {}
    while True:
        i = i + 1
        name = input("введите название: ")
        if name == 'end':
            break
        price = int(input("введите цену: "))
        quantity = int(input("введите количество: "))
        meas = input("введите единицы: ")
        s1 = [i, {'название': name, 'цена': price, 'количество': quantity, 'eд': meas}]
        tL = list(t)
        tL.append(s1)
        t = tuple(tL)
    d = {'название': [], 'цена': [], 'количество': [], 'eд': []}
    for j in t:
        for key in d:
            p = d[key]
            p.append(j[1][key])
            d.update(dict.fromkeys([key], p))
    print(d)
except Exception as err:
    print(f"Ошибка! {err}")
