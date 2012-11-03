import unittest

def func(value=None):
    raise ValueError

def kwargs(k1=None,k2=None):
    print "k1=",k1
    print "k2=",k2
    raise ValueError

class MyTestCase(unittest.TestCase):
    def test_func(self):
        self.assertRaises(ValueError, func)
        self.assertRaises(ValueError, func,1)

    def test_kwargs(self):
        self.assertRaises(ValueError, kwargs,**dict(k1=1))

if __name__ == "__main__":
    unittest.main()