import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print "setUp"

    def test1(self):
        print "test1"

    def test2(self):
        print "test2"

if __name__ == "__main__":
    unittest.main()
