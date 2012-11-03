# -*- coding: utf-8 -*-
from pymorphy import get_morph
morph = get_morph('dicts/ru')
print morph.normalize(u"ЛЮДЕЙ")