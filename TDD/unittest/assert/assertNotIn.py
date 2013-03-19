import unittest


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertNotIn(4, [1,2,3])


if __name__ == "__main__":
    unittest.main()