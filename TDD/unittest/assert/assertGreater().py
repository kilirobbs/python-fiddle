import unittest


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertGreater(3, 2)


if __name__ == "__main__":
    unittest.main()
