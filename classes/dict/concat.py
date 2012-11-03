# http://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python

d1 = {1: 2, 3: 4}
d2 = {5: 6, 7: 9}
d3 = {10: 8, 13: 22}
d4 = {1: 2, 3: 4, 5: 6, 7: 9, 10: 8, 13: 22}

d4 = dict(d1.items() + d2.items() + d3.items())

d4 = dict(d1)
d4.update(d2)
d4.update(d3)