some_list2 = []
some_list2 += ["something"]


d=dict()

#d[14]=d[14].append(18)

oid=1
value=14
d[oid].append(value) if value in d else d[oid]=[value]