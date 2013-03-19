from unittest import main, skip, TestCase
from nose.tools import assert_in

class Test(TestCase):
    @skip("")
    def test_func1(self):
        print "func1"
        assert_in(1,[1,2])

    def test_func2(self):
        print "func2"
        assert_in(1,[1,2])


main()