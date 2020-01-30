start = int(input('Enter number 1: '))
stop = int(input('Enter number 2: '))
step = int(input('Enter number 3: '))


def my_range(start, stop, step):
    k = start
    result = []
    while k < stop:
        result.append(k)
        k += step
    return result


print('List: ', my_range(start, stop, step))
my_range(start, stop, step)
