from git import *
repo = Repo("/Users/nordmenss/git/pg_test")

from git.objects.blob import Blob
# class git.objects.blob.Blob(repo, binsha, mode=None, path=None)
binsha=repo.head.commit.binsha
blob=Blob(repo, binsha,path="schema/public.sql")
print "blob.path=",blob.path
print blob.data_stream.read() 
# TypeError: 'OStream' object is not callable

tree=repo.head.commit.tree
print tree['SCHEMA/public.sql'].__class__
print tree['SCHEMA/public.sql'].data_stream.read() 
try:
	print 'SCHEMA/public.sql' in tree['SCHEMA']
except:
	print "False"

for blob in tree['SCHEMA'].blobs:
	data_stream = blob.data_stream
	print data_stream.read()