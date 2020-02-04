str_1 = input("Enter string: ").split()
if 0 < len(str_1) < 1000:
    for x in str_1:
        print(x.capitalize(), end = ' ')
