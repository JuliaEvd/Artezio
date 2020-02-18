def foo(obj):
    b = [arg for arg in dir(obj) if not arg.startswith('_')]
    return b


o = 'list'
print(foo(o))
