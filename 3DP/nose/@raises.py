import unittest
from nose.tools import raises

class MyTestCase(unittest.TestCase):
    value = None

    @raises(ValueError)
    def test_Exception(self):
        '''this test should pass'''
        raise ValueError 

    @raises(TypeError, ValueError)
    def test_1(self):
        raise ValueError 


if __name__ == "__main__":
    unittest.main()