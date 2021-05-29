def dec(zn):
    def outer(func):
        def inner(a, b):
            if zn == 0:
                try:
                    print(func(a, b))
                except Exception as err:
                    print(err)
            else:
                print(func(a, b))

        return inner

    return outer


z = 1


@dec(z)
def divisor(a, b):
    return a / b


cnt = 0
a = 5
b = 3
while (cnt < 10):
    divisor(a, b)
    a -= 1
    b -= 1
    cnt += 1