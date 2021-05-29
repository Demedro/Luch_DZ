import timeit

def outer(func):
    def inner(a, b):
        start_time = timeit.default_timer()
        func(a, b)
        print(timeit.default_timer() - start_time)
    return inner

@outer
def pl(a, b):
    c = a + b
    return c

@outer
def mi(a, b):
    c = a - b
    return c

@outer
def um(a, b):
    c = a*b
    return c

@outer
def st(a, b):
    c = a**b
    return c

a = 10
b = 20

pl(a, b)
mi(a, b)
um(a, b)
st(a, b)
