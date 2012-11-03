import unittest

# http://docs.python.org/library/unittest.html#assert-methods 


class testclass (unittest.TestCase):
 
	def test_assertEqual(self):
		self.assertEqual(1, 1)

	def test_assertNotEqual(self):
		self.assertNotEqual(1, 2)

	def test_assertTrue(self):
		self.assertTrue(True,True)

	def test_assertFalse(self):
		self.assertFalse(False,False)

	def test_assertFalse(self):
		self.assertIs(88,88)

if __name__ == "__main__":
	unittest.main()