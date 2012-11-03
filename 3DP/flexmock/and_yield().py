from flexmock import flexmock


class cls:
    def log(self):
        return [1, 2, 3]

flexmock(cls).should_receive('log').and_yield('take off', 'flight', 'landing')
for i in cls.log():
    print i

flexmock(cls, log=iter(['take off', 'flight', 'landing']))
for i in cls.log():
    print i