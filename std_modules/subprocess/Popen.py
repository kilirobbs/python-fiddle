import subprocess, os
from subprocess import PIPE, Popen
subprocess.Popen('echo "Hello world!"', shell=True)

outputTuple = Popen(["gcc", "--version"], stdout = PIPE).communicate()
#print outputTuple[0]

outputTuple = subprocess.Popen("gcc --version", stdout = PIPE, shell=True).communicate()
#print outputTuple[0]


outputTuple =subprocess.Popen("gcc --version", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).communicate()
#print outputTuple[0]


outputTuple = Popen(["git", "status","-s"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
#print outputTuple[0]