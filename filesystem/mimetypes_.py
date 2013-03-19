from mimetypes import guess_type
from sys import executable

print guess_type(__file__)
print guess_type("access()")
print guess_type(executable)