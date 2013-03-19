#!/usr/bin/env python
from subprocess import PIPE, Popen, STDOUT

f="/Users/nordmenss/git/FIDDLE/postgresql-fiddle/array/explode.sql"
process = Popen(
    ["psql","-h","127.0.0.1","-p","5432","-U","2nordmenss","-f",f,"postgres"], 
    stdout=PIPE, 
    stdin=PIPE, 
    stderr=STDOUT
)
stdout,stderr=process.communicate()
print stdout,stderr  