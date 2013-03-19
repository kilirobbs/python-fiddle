import pandoc
from os.path import exists

pandoc.PANDOC_PATH = '/usr/local/bin/pandoc'
print exists(pandoc.PANDOC_PATH)
doc = pandoc.Document()
md="/Users/nordmenss/git/Sublime-Shell-build/README.md"
print exists(md)
doc.markdown = open(md).read()
print doc.rst
