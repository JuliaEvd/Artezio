def chain(*args):
    for arg in args:
        for i in arg:
            yield i


my_list = chain([1, 2, 3], [4, 5, 6])
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
