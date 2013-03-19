# -*- coding: utf-8 -*-
import os

namelist=["line1","line2"]

f = open('test.txt', 'w') # write
f.writelines(namelist)
for name in namelist:
    f.write(name)
f.close()

#open('test.txt', 'w').write(content) # one liner

f = open('test.txt', 'r+') # read & write
f.writelines(namelist)
f.close()

filename="not_existing_path/filename.sql"

if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))


open("dict.txt","w").write(unicode(dict()))
print open("dict.txt").read()
