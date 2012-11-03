import unittest
import sys

class MyTestCase(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

if __name__ == "__main__":
    unittest.main()