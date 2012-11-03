# http://docs.python.org/distutils/index.html

from distutils.core import setup
setup(name='foo',
      #platforms = ["POSIX", "Windows"],
      #platforms =['All'],
      platforms = ["Linux", "Windows", "MacOS X"]
      #platforms = ["MacOS X"]
)