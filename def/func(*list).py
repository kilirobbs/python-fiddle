def func(host=None, port=None):
    print host, port

func(*["127.0.0.1", 5432])


def set(section, key, value):
    print section, key, value

set(*"section.key".split(".") + ["value"])
