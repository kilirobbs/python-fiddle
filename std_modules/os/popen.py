import os

stream = os.popen("ls")
print stream.read()