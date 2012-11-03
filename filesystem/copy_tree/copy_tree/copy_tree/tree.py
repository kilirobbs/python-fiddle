import os


def paths(path):
    result =[]
    for parent, dirs,files in os.walk(path,topdown=True):
        try:
            dirs.remove('.git')
        except ValueError:
            pass
        for dir in dirs:
            result.append(os.path.join(parent, dir))
        for file in files:
            if file[0:1] !=".": #.DS_Store
                result.append(os.path.join(parent, file))
    return result

result =paths("/Users/nordmenss/git/pg_test")
print "\n".join(result)
