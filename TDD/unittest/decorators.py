import unittest

# some magic code will be added here later

class DummyTest(unittest.TestCase):
  @for_examples(1, 2)
  @for_examples(3, 4)
  def test_is_smaller_than_four(self, value):
    self.assertTrue(value < 4)

  @for_examples((1,2),(2,4),(3,7))
  def test_double_of_X_is_Y(self, x, y):
    self.assertEqual(2 * x, y)

if __name__ == "__main__":
  unittest.main()