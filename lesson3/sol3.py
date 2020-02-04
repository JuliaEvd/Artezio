maximum = 0


def foo(a, b, c, d):
    max_args = max(a, b, c, d)
    ar_mean = (a + b + c + d) / 4
    global maximum
    if maximum < max_args:
        maximum = max_args
    return ar_mean, maximum


print(foo(1, 2, 3, 4))
print(foo(-3, -2, 10, 1))
print(foo(7, 8, 8, 1))
