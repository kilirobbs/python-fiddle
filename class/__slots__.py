class simple_class:
    pass

class fast_class:
    __slots__ = ["a", "b"]

print simple_class().__dict__  # {}
print fast_class().__dict__  # {}