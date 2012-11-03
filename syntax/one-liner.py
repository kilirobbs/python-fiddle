print "1" if True else ""

print [i for i in range(1, 11)]
print map(int, range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print [item.lower() for item in ["Foo", "Bar"]]

print [i for i in range(1, 11) if i<5]
# [1, 2, 3, 4]


print [i for i in range(1, 11) if i<5]

print ",".join(["'"+v+"'" for v in ["Foo", "Bar"]])