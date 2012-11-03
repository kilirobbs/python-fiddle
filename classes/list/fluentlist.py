class line(object):
    host = None
    port = None
    db = None
    user = None
    _password = None
    comment = None

    def __init__(self, host="*", port="*", db="*", user="*", password=None, comment=None):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.comment = comment

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, v):
        if v:
            self._password = v
        else:
            raise ValueError("Empty password")

    def __str__(self):
        return self.host

    def __repr__(self):
        return "%(host)s:%(port)s:%(db)s:%(user)s:%(password)s%(comment)s" % \
            {
                "host": self.host,
                "port": self.port,
                "db": self.db,
                "user": self.user,
                "password": self.password,
                "comment": " # %s" % self.comment if self.comment else ""
            }


class fluentlist(list):
    def __getattribute__(self, k):
        try:  # exists
            return super(list, self).__getattribute__(k)
        except AttributeError:  # not exists
            def subclass():
                class selector(self.__class__):
                    values = super(self.__class__, self).__getslice__(0, 2)
                    attr = k

                    def __init__(self, value=None):
                        super(fluentlist, self).__init__()
                        values = self.values
                        attr = self.attr
                        filtered = filter(lambda x: getattr(x, attr) == value, values)
                        map(self.append, filtered)
                return selector
            return subclass()

    def __str__(self):
        return str(self[:])


class items(fluentlist):
    def __init__(self, data=[]):
        super(self.__class__, self).__init__(data)

    @property
    def password(self):
        print len(self[:])
        if len(self[:]) > 0:
            pass

l = items([line(password="1"), line(password="1")])
print l
print l.host("*")
print l.host("*").user("*").db("*").user("*").password