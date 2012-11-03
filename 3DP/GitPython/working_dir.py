from git import Repo
repo = Repo("/Users/nordmenss/git/pg_test/SCHEMA")

print repo.working_dir
print repo._working_tree_dir
