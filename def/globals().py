def f(a, b):
    result = a + b
    print result
    return result

a = f
globals()['a'](1, 2)


