print "5433" > 0
print "not integer" > 0
print ""
print "5433".isdigit()
print "not integer".isdigit()


str = "h3110 23 cat 444.4 rabbit 11 2 dog"
print [int(s) for s in str.split() if s.isdigit()]
# [23, 11, 2]