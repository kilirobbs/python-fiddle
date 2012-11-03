dirs=["/Users/nordmenss/git/repo1","/Users/nordmenss/git/repo2"]
filename="/Users/nordmenss/git/repo1/filename"

for dir in dirs:
    if filename.startswith(dir+"/"):
        print dir
