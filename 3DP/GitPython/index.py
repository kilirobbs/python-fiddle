from git import *
repo = Repo("/Users/nordmenss/git/Sublime-autogit")

index = repo.index
print index
for stage, blob in index.iter_blobs():
    print "blob=", blob
print "\n\n\n\n"
for (path, stage), entry in index.entries.iteritems():
    print "path=", path, "stage=", stage, "entry=", entry
