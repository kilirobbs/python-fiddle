#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup file for setuppy package """

from setuptools import setup, find_packages
from os.path import abspath, dirname, join

dir=dirname(abspath(__file__))
description = open(join(dir,'description')).read()
readme = open(join(dir,'README.rst')).read()