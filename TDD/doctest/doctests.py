#! /usr/bin/python

import sys

def mult(a,b):
    """
    >>> print >> sys.stderr, "----- Print to stderr -----"
    >>> mult(2,2)
    4
    """
    return a*b

class A():
    """
    >>> a = A()
    >>> a.atr
    4
    """

    atr = 4

    def mult(self,a):
        """
        >>> a = A()
        >>> a.mult(2)
        8
        """
        return a * self.atr
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    #doctest.testmod(verbose=True) # verbose output
    doctest.testfile("tests.txt") # execute tests from file