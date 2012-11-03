import sys


print sys.argv
sys.argv.append("--exclude-schema=pg_catalog,informaton_schema")

print sys.argv

print "sys.argv:"
for argv in sys.argv:
	if argv.find("=")>0:
		if argv.split("=")[0]=="--exclude-schema":
			print argv.split("=")[1].strip().split(",")
