import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
res='[{ \
        "title": "title test", \
        "description": "desc test"  \
        }, \
        { \
        "title": "title test 2", \
        "description": "desc test 2"  \
        }] '
data = json.loads(res) 

for item in data:
	# print item["title"]
    # now song is a dictionary
	for attribute, value in item.iteritems():
		print attribute, value # example usage

# description desc test 
# title title test 
# description desc test 2 
#  title title test 2
