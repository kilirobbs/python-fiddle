from unittest import main,skip,TestCase
from nose.tools import assert_in, assert_is_not_none, assert_is_instance, eq_, ok


class TestCase(TestCase):
    @skip("")
    pass

if __name__ == "__main__":
    main()