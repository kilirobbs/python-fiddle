#!/usr/bin/env python
from unittest import main, skip,TestCase

class Test(TestCase):
    def test_pass(self):
        pass

    @skip("skip message")
    def test_skip(self):
        pass


if __name__ == "__main__": # pragma: no cover
    main()