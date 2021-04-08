d = {'12': 'зима', '1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето',
     '8': 'лето', '9': 'осень', '10': 'осень', '11': 'осень'}
# for i in d:
#     print(i)
#     print(d[i])
# mon = int(input("введите число: "))
mon = input("введите значение: ")
if mon in d.keys():
    print(d.get(mon))
elif mon in d.values():
    for k, v in d.items():
        if mon == v:
            print(k)
else:
    print('месяца нет')