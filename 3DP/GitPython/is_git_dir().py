from git.repo.fun import is_git_dir

print is_git_dir(".")
print is_git_dir("/Users/nordmenss/git/1")
print is_git_dir("/Users/nordmenss/git/1/.git")
