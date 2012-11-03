# http://docs.python.org/library/stdtypes.html#mapping-types-dict
print {"one": "one"}
print dict(one=1, two=2)
# print dict(1=1, 2=2) # SyntaxError: keyword can't be an expression
print dict({1: 1, 2: 2})
print dict({'one': 1, 'two': 2})
print dict(zip(('one', 'two'), (1, 2)))
print dict([['two', 2], ['one', 1]])

d = dict()
d[(1, 2)] = 3
