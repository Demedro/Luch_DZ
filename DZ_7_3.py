def dec(ex):
    def outer(func):
        def inner(a, b):
            try:
                func(a, b)
            except ex as err:
                print(err)

        return inner

    return outer


ex = ZeroDivisionError,TypeError

@dec(ex)
def divisor(a, b):
    return a / b

@dec(ex)
def con(a, b):
    return len(a + b)

con(1, 2)