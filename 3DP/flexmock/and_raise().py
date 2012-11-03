from flexmock import flexmock


class classname:
    def badfunc(self):
        pass

# http://has207.github.com/flexmock/user-guide.html#exceptions

flexmock(classname).\
    should_receive('badfunc').and_raise(ValueError, "error desc")


classname().badfunc()