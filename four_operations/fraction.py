# -*- coding: utf-8 -*-

class fraction(object):
    def __init__(self):
        self.numerator = None
        self.denominator = None

    def setNumerator(self, numerator):
        self.numerator = numerator

    def setDenominator(self, denominator):
        self.denominator = denominator

    def toString(self):
        a = int(self.numerator)
        b = int(self.denominator)
        if b == 1:
            return str(a)
        else:
            if a > b:
                c = int(a / b)
                d = int(a % b)
                if d == 0:
                    return str(c)
                else:
                    return str(c) + "`" + str(d) + "/" + str(b)
            elif a == b:
                return "1"
            else:
                return str(a) + "/" + str(b)