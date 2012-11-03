# tests.py
import unittest
from ddt import ddt, data

def larger_than_two(value):
	return value>2

def file_type(value):
	return value == file

@ddt
class FooTestCase(unittest.TestCase):

    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(larger_than_two(value))

    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self, value):
        self.assertFalse(larger_than_two(value))

    @data(file) 
    def test_file(self, value):
    	print "never executed"
        self.assertTrue(file_type(value))

if __name__ == "__main__":
    unittest.main()