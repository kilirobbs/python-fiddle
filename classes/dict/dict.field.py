class mydict(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


a = mydict(no="way", bad="code")
print a.no