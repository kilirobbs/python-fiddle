import unittest

class TestCase(unittest.TestCase):
    value = None

    def setUp(self):
        self.value = "88"

    def test(self):
        self.assertNotIsInstance(self.value, int, "need string")
        # AssertionError: not datetime

if __name__ == "__main__":
    unittest.main()
