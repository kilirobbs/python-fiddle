from git import Repo,Git
repo = Repo.init("/Users/nordmenss/git/sublime-helper")
# http://packages.python.org/GitPython/0.3.0/tutorial.html#the-commit-object
#repo.git.add('-A')
#repo.index.commit("commit") # hooks not run


# 1 Git(repo.working_dir).execute(["git", "commit", "-m", "'message'"])

print repo.git.commit(m=' "%s"' % '"message"'.replace('"','\\"'))
print "ok"