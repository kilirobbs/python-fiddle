from git import *
repo = Repo("/Users/nordmenss/git/applescript-fiddle")

for diff in repo.index.diff(None):
    print "%(path)s %(name)s %(deleted)s %(diff)s %(new_file)s" % \
        {
            "path": diff.a_blob.path,
            "name": diff.a_blob.name,
            "deleted": "deleted" if diff.deleted_file else "",
            "diff": "diff" if diff.diff else "",
            "new_file": "new_file" if diff.new_file else "",
            "renamed": "renamed" if diff.renamed else ""
        }

print "\n" * 10


def deleted(repo):
    for diff in repo.index.diff(None).iter_change_type("D"):
        print diff.a_blob.path

deleted(repo)
