from flexmock import flexmock

flexmock(__builtins__).should_call('open')
flexmock(__builtins__).should_receive('open').at_most().with_args('foo.txt').and_return(
    flexmock(read=lambda: 'some data')
)
print open('foo.txt').read()    # at_most
print open('read.py').read()    # at_most
