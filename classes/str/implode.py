print ".".join(['s', 'p', 'a', 'm', 'm', 'y'])


# print ".".join(['1','2',None,None,'3']) # Exception


print "\n".join(['1', "", "", '2'])

print "\n".join(filter(None, ["1", "2"]))

print "\n".join(filter(None, [None, None])) is None
# False