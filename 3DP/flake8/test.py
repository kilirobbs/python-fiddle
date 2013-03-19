#!/usr/bin/python
import sys
from flake8.run import git_hook

COMPLEXITY = 10
STRICT = False

if __name__ == '__main__':
    print git_hook(complexity=COMPLEXITY, strict=STRICT, ignore='E501'))