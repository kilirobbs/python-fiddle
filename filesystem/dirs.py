import os


def directories(path):
    for parent, dirs, files in os.walk(path):
        return map(lambda d: os.path.join(parent, d), dirs)

print directories(os.path.expanduser("~/git"))