def count_s(string):
    s = {}
    for x in string:
        count = 0
        for y in string:
            if x == y:
                count += 1
        rec = {x: count}
        s.update(rec)
    return s


q = input("Enter string: ")
print(count_s(q))