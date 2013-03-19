#!/usr/bin/env python
class fluentdict(dict):
    attr="attr"

    def __getattribute__(self, k):
        try:
            return dict.__getattribute__(self, k)
        except AttributeError:
            if self[k].__class__==dict:
                return fluentdict(self[k])
            else:
                return self[k]

    def __setattr__(self, key, value):
        self[key] = value


a = mydict(no="way", bad="code")
print a.attr
print a.no
print a.not_existing