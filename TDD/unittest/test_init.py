# http://stackoverflow.com/questions/88325/how-do-i-unit-test-an-init-method-of-a-python-class-with-assertraises
import unittest

class MyClass:
	def __init__(self, foo):
		if foo != 1:
			raise ValueError("foo is not equal to 1!")

class TestFoo(unittest.TestCase):
    def failUnlessRaises(self, excClass, callableObj, *args, **kwargs):
        try:
            callableObj(*args, **kwargs)
        except excClass, excObj:
            return excObj # Actually return the exception object
        else:
            if hasattr(excClass,'__name__'): excName = excClass.__name__
            else: excName = str(excClass)
            raise self.failureException, "%s not raised" % excName

    def testInsufficientArgs(self):
        foo = 0
        excObj = self.failUnlessRaises(ValueError, MyClass, foo)
        self.failUnlessEqual(excObj[0], 'foo is not equal to 1!')

if __name__ == "__main__":
	unittest.main()