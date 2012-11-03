import os
import shutil


class directory():
    path = None
    dirs = []
    files = []

    def __init__(self, path):
        self.path = path
        self.walk()

    def walk(self):
        for parent, dirs, files in os.walk(self.path):
            for dir in dirs:
                path = os.path.join(parent,dir)
                self.dirs.append(directory(path))
            for file in files:
                filename = os.path.join(parent,file)
                self.files.append(filename)
            break

    @property
    def is_empty(self):  # return True if dir is empty
        return len(self.files) == 0

    def rm(self):
        shutil.rmtree(self.path)


class fs_tree(directory):  # filesystem
    root = None
    dirs = []
    ignore = []

    def scan(self):  # scan directory for dirs&files
        self.walk()

    def rm(self):
        pass

    def write(self, filename, content):
        pass

    def is_exists(self, filename):
        pass

    def read(self, filename):
        pass


def paths(path):
    result = []
    for parent, dirs, files in os.walk(path,topdown=True):
        try:
            dirs.remove('.git')
        except ValueError:
            pass
        for dir in dirs:
            result.append(os.path.join(parent, dir))
        for file in files:
            if file[0:1] != ".": #.DS_Store
                result.append(os.path.join(parent, file))
    return result

result = paths("/Users/nordmenss/git/pg_test")
print "\n".join(result)
