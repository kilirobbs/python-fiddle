from git import *
repo = Repo("/Users/nordmenss/git/python/PyDefaults")

head = repo.head            # the head points to the active branch/ref
master = head.reference # current branch

print master
# change commit by hash
master.commit='59cc480b480ace8b39b459edcff45dc56f07c8dc'
# or by steps
# master.commit = 'HEAD~10'  
print master.commit.message

for commit in repo.iter_commits(master, max_count=-1, skip=-1):
	print commit.__class__, "hexsha=",commit.hexsha