# http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception

import unittest

def myfunc():
	raise ValueError

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, myfunc)


if __name__ == "__main__":
	unittest.main()