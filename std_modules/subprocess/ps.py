#!/usr/bin/env python
from subprocess import PIPE, Popen

cmd="ps cax | grep say | grep -v grep"
process = Popen(cmd,shell=True,stdout=PIPE)
stdout,stderr = process.communicate()
print stdout,stderr 