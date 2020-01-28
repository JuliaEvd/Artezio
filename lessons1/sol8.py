my_dict = {'a':123, 'b':321, 'c': 0,'d':80, 'e':900, 'f': 901}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)