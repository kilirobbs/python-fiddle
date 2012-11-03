# -*- coding: utf-8 -*-

def numending_rus(num, engings):
    num = num % 100
    if num >= 11 and num <= 19:
        return engings[2]
    else:
        i = num % 10
        if i == 1:
            return engings[0]
        else:
            if i in [2, 3, 4]:
                return engings[1]
            else:
                return engings[2]

 print numending_rus(2, ["час", "часа", "часов"])