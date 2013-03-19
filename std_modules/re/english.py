#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import compile,sub


def english(text):
    return bool(compile('^[a-zA-Z\-]+\Z').match(text))


print sub("[^\w\d\ \-\_]", "_","word18-space")