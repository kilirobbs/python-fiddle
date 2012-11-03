# http://stackoverflow.com/questions/19151/build-a-basic-python-iterator


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print c


class sublist(list):
    def __iter__(self):
        for i in self[:]:
            yield i

print ""
for v in sublist([1, 2, 3]):
    print v