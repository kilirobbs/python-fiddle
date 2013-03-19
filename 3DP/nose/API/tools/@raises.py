import unittest
from nose.tools import raises

class MyTestCase(unittest.TestCase):
    value = None

    @raises(Exception)
    def test_AnyExceptions(self):
        raise IOError 

    @raises(ValueError)
    def test_ValueError(self):
        '''this test should pass'''
        raise ValueError 

    @raises(TypeError, ValueError)
    def test_EnumError(self):
        raise ValueError 


if __name__ == "__main__":
    unittest.main()