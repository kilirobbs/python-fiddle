#!/usr/bin/env python
def exists(l1, l2):
    return ''.join(map(str, l2)) in ''.join(map(str, l1))

print exists([1,2,3],[1,2])
print exists([1,2],[1,2])
print exists([1,2],[1,2,3])