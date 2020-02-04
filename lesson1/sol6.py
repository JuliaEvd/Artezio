n = int(input('Enter a number: '))
elements = n + 1
dictionary = {}
for x in range(1, elements):
    dictionary[x] = x * x
print(dictionary)
