# http://www.ibm.com/developerworks/ru/library/l-pymeta/

def class_with_method(func):
	class klass: pass
	setattr(klass, func.__name__, func)
	return klass

def say_foo(self): 
	print 'foo'
		
Foo = class_with_method(say_foo)
foo = Foo()
foo.say_foo()



from new import classobj
Foo2 = classobj('Foo2',(Foo,),{'bar':lambda self:'bar'})
Foo2().bar()
Foo2().say_foo()