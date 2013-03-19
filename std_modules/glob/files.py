from glob import glob
from os.path import dirname, join
print glob(
    join(dirname(dirname(__file__)),"*")
)