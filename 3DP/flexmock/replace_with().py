from flexmock import flexmock


class cls:
    def func(self, value):
        return "func(%s)" % value

flexmock(cls).should_receive('func').replace_with(lambda x: x > 0)
print cls().func(88)
 # shorthand
flexmock(cls, func=lambda x: x > 0)
print cls().func(88)


def func(value):
    print "custom func with %s" % value

flexmock(cls, func=func)
cls().func(88)
