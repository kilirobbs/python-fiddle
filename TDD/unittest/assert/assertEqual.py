import unittest


class MyTestCase(unittest.TestCase):
    value = None

    def setUp(self):
        self.value = 88

    def test(self):
        self.assertEqual(self.value, 88)

    def test(self):
        self.assertEqual(self.value, 88,88)

if __name__ == "__main__":
    unittest.main()