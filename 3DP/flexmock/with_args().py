from flexmock import flexmock


class cls:
    def func(self, value):
        return "func(%s)" % value

flexmock(cls).should_receive('func').with_args(14)
print cls().func(14)  # error if not 14
print cls().func(88)

flexmock(cls).should_receive('func').with_args(int)
print cls().func(14)  # int only
