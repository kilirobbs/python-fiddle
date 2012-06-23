import sys
sys.path.append("unittest")
sys.path.append("doctest")
import unittest
import test_account

class TestSuite:
    def __init__(self):
        pass

suite = unittest.TestLoader().loadTestsFromModule(test_account)
unittest.TextTestRunner(verbosity=1).run(suite)