def files_iterator(path):
    for parent, dirs, files in os.walk(path,topdown=True):
        try:
            dirs.remove('.git')
        except ValueError:
            pass
        for filename in files:
            path, ext = os.path.splitext(filename)
            if ext in [".oid", ".sql", ".preferences"]:
                yield os.path.join(parent, filename)
