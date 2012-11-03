# http://docs.python.org/library/collections.html#collections.Counter
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
	cnt[word] += 1
print cnt

print "cnt['not_existing']=",cnt["not_existing"]