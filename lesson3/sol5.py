def foo(s):
    s = s.split()
    return min(map(float, s), key=abs)


my_list = input()
print(foo(my_list))
