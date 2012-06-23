from subprocess import call
call(["ls", "-l"])


stream = os.popen("ls")
print stream.read()