import unittest
import sys

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

if __name__ == "__main__":
    unittest.main()