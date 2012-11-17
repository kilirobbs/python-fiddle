from glob import glob
import os

os.chdir("/Users/nordmenss/git/Sublime-autopep8")
print glob("/Users/nordmenss/git/*/setup.py")
print glob("setup.py")

def files(folders):
    return sum(map(lambda d:glob("%s/*/setup.py" % d),folders), [])

print files(["/Users/nordmenss/git/PyMacOS"])
print files(["/Users/nordmenss/git"])