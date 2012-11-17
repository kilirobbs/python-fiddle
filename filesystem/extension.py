import os
# http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
fileName, ext = os.path.splitext('/path/to/somefile.ext.ext2')
print "fileName=", fileName
print "ext=", ext

fileName, ext = os.path.splitext('/path/to/count("any").sql')
print "fileName=", fileName
print "ext=", ext


print os.path.splitext('.DS_Store')
print os.path.splitext('/path/to/basename')