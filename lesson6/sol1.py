class EvenIterator(object):

    def __init__(self, list):
        self.list = list
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 2
        if self.count <= len(self.list):
            return self.list[self.count - 2]
        else:
            raise StopIteration


my_list = EvenIterator([0, 1, 2, 3, 4, 5])
for i in my_list:
    print(i)
