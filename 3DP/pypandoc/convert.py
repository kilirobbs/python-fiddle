import pypandoc
md="/Users/nordmenss/git/Sublime-Shell-build/README.md"
output = pypandoc.convert(md, 'rst')

print output
