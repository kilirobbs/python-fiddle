# -*- coding: utf-8 -*-
import re


def english(text):
    return bool(re.compile('^[a-zA-Z\-]+\Z').match(text))