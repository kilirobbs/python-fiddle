from flexmock import flexmock


class cls:
    def func(self, value):
        return "func1(%s)" % value


flexmock(cls)
cls.should_receive('func').and_return('out')
print cls.func()