from git import *
repo = Repo("/Users/nordmenss/git/pg_test")

tree=repo.head.commit.tree
path="SCHEMA/public/OPERATOR/>=(ip4,ip4).sql"
print tree[path].__class__
print tree[path].data_stream.read() 