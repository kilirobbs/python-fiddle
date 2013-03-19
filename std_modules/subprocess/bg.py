from subprocess import PIPE, Popen, STDOUT

def bg(command):
    return Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
