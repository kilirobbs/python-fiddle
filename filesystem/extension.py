from os.path import splitext
# http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
fileName, ext = splitext('/path/to/somefile.ext.ext2')
print "fileName=", fileName
print "ext=", ext

fileName, ext = splitext('/path/to/count("any").sql')
print "fileName=", fileName
print "ext=", ext


print splitext('.DS_Store')
print splitext('/path/to/basename')
print splitext('/path/to/setup.py')