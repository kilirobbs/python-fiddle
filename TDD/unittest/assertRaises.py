import unittest

def myfunc():
    raise ValueError

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, myfunc)


if __name__ == "__main__":
    unittest.main()
