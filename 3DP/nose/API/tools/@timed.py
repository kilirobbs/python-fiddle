import unittest
import time
from nose.tools import timed

class MyTestCase(unittest.TestCase):
    value = None

    @timed(.1)
    def test_time(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()