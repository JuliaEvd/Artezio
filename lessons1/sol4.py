my_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for x in my_list:
    if len(x) >= 2 and x[0] == x[-1]:
        count += 1
print(count)
