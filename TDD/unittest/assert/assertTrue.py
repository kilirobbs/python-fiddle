import unittest

class MyTestCase(unittest.TestCase):
    value = None

    def setUp(self):
        self.value = True

    def test(self):
        self.assertTrue(self.value, True)


if __name__ == "__main__":
    unittest.main()
