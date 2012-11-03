import os
from subprocess import PIPE, Popen, STDOUT

def shell(command):
    process = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
    r = process.communicate()
    if process.returncode != 0:
        raise SystemError(r[0])
    else:
        # remove line break
        return "\n".join(r[0].splitlines())

class section_key():
    section = None
    name = None
    def __init__(self,section,name):
        self.section=section
        self.name=name

    def unset(self):
        try:
            command='git config --file %(filename)s --unset %(section)s.%(key)s' % \
            {
                "filename" : str(self.section.file),
                "section" : str(self.section),
                "key" : self.name
            }
            shell(command)
            return True
        except:
            return False

    def delete(self):
        self.unset()

    @property
    def value(self):
        command='git config --file %(filename)s %(section)s.%(key)s' % \
        {
            "filename" : str(self.section.file),
            "section" : str(self.section),
            "key" : self.name
        }
        return shell(command)

    def exists(self):
        try:
            self.value
            return True
        except:
            return False

    def __str__(self):
        try:
            return self.value
        except:
            return ""

class section(object):
    file = None
    name = None

    def __init__(self,file,name=None):
        self.file = file
        self.name = name

    def __setattr__(self, k,v):
        if hasattr(self,k):
            if getattr(self,k).__class__==section_key:
                command='git config --file %(filename)s %(section)s.%(key)s "%(value)s"' % \
                {
                    "filename" : str(self.file),
                    "section" : self.name,
                    "key" : k,
                    "value" : str(v) # str() !
                }
                shell(command)
            else:
                super(section, self).__setattr__(k, v)

    def __getattribute__(self, key):
        try: # exists
            return super(section,self).__getattribute__(key)
        except AttributeError: # not exists
            return section_key(self,key)

    def unset(self,key):
        return section_key(self,key).unset()

    def __str__(self):
        return self.name

class gitconfig(object):
    filename = None

    def __init__(self, filename):
        self.filename = filename

    def __getattr__(self, name):
        # called if self.key not exists 
        return section(self,name)

    @property
    def exists(self):
        return os.path.exists(self.filename)

    def delete(self):
        if self.exists:
            os.unlink(self.filename)

    def __str__(self):
        return self.filename

config = gitconfig("/Users/nordmenss/.myweather")
print config.s.key
config.s.key=88
print config.s.key
config.s.unset("key")
config.s.key.delete()
config.delete()