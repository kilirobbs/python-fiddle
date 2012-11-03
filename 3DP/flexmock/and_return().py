from flexmock import flexmock


class cls:
    def get(self):
        return "get_name"

flexmock(cls).should_receive('get').and_return('a')
print cls.get()  # a
# Multiple return values
# http://has207.github.com/flexmock/user-guide.html#multiple-return-values
flexmock(cls).should_receive('get').and_return('a').and_return('b')

print cls.get()  # a
print cls.get() # b