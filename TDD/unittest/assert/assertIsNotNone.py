import unittest
from datetime import datetime


class TestCase(unittest.TestCase):
    def test(self):
        self.assertIsNotNone(self.now)
        # AssertionError: not datetime

if __name__ == "__main__":
    unittest.main()
