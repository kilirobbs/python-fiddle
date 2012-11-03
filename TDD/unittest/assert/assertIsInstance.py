import unittest
from datetime import datetime

class TestCase(unittest.TestCase):
    now = None

    def setUp(self):
        #self.now = datetime.now()
        self.now = 88

    def test(self):
        self.assertIsInstance(self.now, datetime, "not datetime")
        # AssertionError: not datetime

if __name__ == "__main__":
    unittest.main()
