from flexmock import flexmock


class classname:
    def func(self):
        print "func"

    def never(self):
        print "never"

# http://has207.github.com/flexmock/user-guide.html#exceptions

flexmock(classname).\
    should_receive('never').never()


classname().func()
classname().never()