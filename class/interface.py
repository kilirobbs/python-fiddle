from abc import ABCMeta, abstractmethod, abstractproperty
class Movable():
    __metaclass__=ABCMeta
    x=None
    @abstractmethod
    def move():
	"""move object"""
    
    @abstractproperty
    def speed():
	"""object speed"""

class Car(Movable):
	def __init__(self):
		self.speed = 10
		self.x = 0

	def move(self):
		self.c += self.speed

	def speed(self):
		return self.speed
    
assert issubclass(Car, Movable)
assert isinstance(Car(), Movable