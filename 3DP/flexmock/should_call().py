from flexmock import flexmock


class classname:
    def get_name(self):
        return "get_name"

flexmock(classname).should_call('get_name').and_return(str, object, None)
# flexmock(classname).should_call('get_name').and_return(float)
print classname.get_name()