import unittest


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertGreaterEqual(3, 3)


if __name__ == "__main__":
    unittest.main()
