from flexmock import flexmock


def write(value):
    print value

flexmock(__builtins__).should_receive('open').with_args('foo.txt', 'w').and_return(
    flexmock(write=write)
)
open('foo.txt', 'w').write("text")
# but we dont want just open...
# print open('foo.txt').read()  # flexmock.MethodSignatureError:

flexmock(__builtins__).should_call('open').with_args('foo.txt')
print open('foo.txt').read()
