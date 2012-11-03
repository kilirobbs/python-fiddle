import subprocess

print "\nsubprocess.call(command)"
result = subprocess.call(["ls", "-l"])
print "result=", result

print "\n\n\nsubprocess.call(command,shell=True)"
result = subprocess.call(["ls", "-l"],shell=True)
print "result=",result