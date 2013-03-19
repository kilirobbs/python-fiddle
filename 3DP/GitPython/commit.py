from git import Repo
repo = Repo("/Users/nordmenss/git/sublime_helper")
index = repo.index
repo.git.add('-A')
for diff in index.diff(None):
    print diff.a_blob.name
#index.add([diff.a_blob.name for diff in index.diff(None)])
#index.commit('message')