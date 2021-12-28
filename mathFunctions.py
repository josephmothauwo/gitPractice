def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    res = 0
    for i in range(x):
        res += y
    return res
