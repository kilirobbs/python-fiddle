#!/usr/bin/env python
from nose.tools import assert_is_instance
from dictcls import dictcls

assert_is_instance(1,int)

assert_is_instance(dictcls(),dict)