import os

namelist=["line1","line2"]

f = open('test.txt', 'w') # write
f.writelines(namelist)
for name in namelist:
    f.write(name)
f.close()

f = open('test.txt', 'r+') # read & write
f.writelines(namelist)
f.close()