import os


def rootdirs(path):
    for parent, dirs, files in os.walk(path):
        return map(lambda d: os.path.join(parent, d), dirs)

print rootdirs(os.path.expanduser("~/git"))