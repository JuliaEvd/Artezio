my_list_1 = input("Enter list 1: ")
my_list_2 = input("Enter list 2: ")
list_new = list(set(my_list_1) ^ set(my_list_2))
print(list_new)