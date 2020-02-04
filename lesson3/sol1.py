def sqrt(col):
    a = []
    for i in col:
        a.append(i * i)
    return a


def even(col):
    a = []
    for i in range(len(col)):
        if i % 2 == 0:
            a.append(col[i])
    return a


def cub(col):
    a = []
    for i, j in enumerate(col):
        if j % 2 == 0 and i % 2 != 0:
            a.append(j ** 3)
    return a


my_list = [1, 2, 3, 4, 5, 6, 6]
print(sqrt(my_list))
print(even(my_list))
print(cub(my_list))
