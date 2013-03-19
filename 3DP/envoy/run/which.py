import subprocess


def cmd_exists(cmd):
    return subprocess.call(["type", cmd], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

print cmd_exists("python2.6")