from os import chdir
import nose

d="/Users/nordmenss/git/PyEarthTools"
chdir(d)
nose.main(argv=['nose', '--verbose'])