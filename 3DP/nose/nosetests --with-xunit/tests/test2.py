#!/usr/bin/env python
from unittest import main, skip,TestCase

class Test(TestCase):
    def test_pass2(self):
        pass

    @skip("")
    def test_skip2(self):
        pass


if __name__ == "__main__": # pragma: no cover
    main()