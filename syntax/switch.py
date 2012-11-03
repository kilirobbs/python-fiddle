# http://bytebaker.com/2008/11/03/switch-case-statement-in-python/
value = "a"
x=1

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)
print result

result = {
  'a' or "A": "1-st",
  'b': '2-st',
  'c': '3-st'
}["d"]
print result