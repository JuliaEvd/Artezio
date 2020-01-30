number = int(input('Enter number: '))


def square(number):
    count = 0
    for i in range(0, number + 1):
        if i % 2 != 0:
            print(i * i)
            count += 1
            print('Odd number all:', count)


square(number)
