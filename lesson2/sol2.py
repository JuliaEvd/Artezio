a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))


def solution(a,b,c):
    count = 0
    for i in range(a, b+1):
        if i % c == 0:
            count += 1
    print("Чисел, делящихся на", c, ":\n", count)


solution(1,3,1)
