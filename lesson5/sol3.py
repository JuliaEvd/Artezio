class Observable(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        s = self.__class__.__name__
        return '{}({})'.format(s, ', '.join('{}={}'.format(key, val)
                                            for key, val in self.__dict__.items() if not key.startswith('_')))


class X(Observable):
    pass


x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)
