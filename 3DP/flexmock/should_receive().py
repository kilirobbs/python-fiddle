from flexmock import flexmock


class cls:
    def func1(self, value):
        return "func1(%s)" % value

    def func2(self, value):
        return "func2(%s)" % value

flexmock(cls).should_receive('func1').and_return('vooosh!')
print cls().func1(14)
print cls().func2(88)
