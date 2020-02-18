def cycle(my_iter):
    while True:
        for i in my_iter:
            yield i


my_list = [1, 2, 3, 4]
res = cycle(my_list)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
