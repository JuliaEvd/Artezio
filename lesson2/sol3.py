number = int(input('Enter number: '))


def factorial():
    f = 1
    for i in range(1, number + 1):
        f *= i
        print(f)


factorial()
