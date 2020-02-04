string = input('Enter string: ')
if len(string) < 2:
    print('Empty string')
else:
    string_1 = string[:2]
    string_2 = string[-2:]
    new_string = string_1 + string_2
    print(new_string)
