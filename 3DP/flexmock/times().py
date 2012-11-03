from flexmock import flexmock


class classname:
    def func(self):
        return "get_name"

flexmock(classname).should_receive('func').times(3)
classname.func()
classname.func()
classname.func()
classname.func()