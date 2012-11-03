def test_var_kwargs(farg, **kwargs):
    kwargs["db"] = "db_value"
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)

test_var_kwargs(1)

# http://stackoverflow.com/questions/5710391/python-dict-to-kwargs-is-possible
test_var_kwargs(1, **{"id": 88})
