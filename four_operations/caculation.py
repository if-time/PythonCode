# -*- coding: utf-8 -*-
import fraction


class caculation(object):

    def caculate(self, op, fraction1, fraction2):
        result = fraction.fraction()
        n1 = int(fraction1.numerator)
        d1 = int(fraction1.denominator)
        n2 = int(fraction2.numerator)
        d2 = int(fraction2.denominator)
        if op == "+":
            if d1 != d2:
                n1 = n1 * d2
                n2 = n2 * d1
                d1 = d1 * d2
                result.setNumerator(n1 + n2)
                result.setDenominator(d1)
                result = self.reduction(result)
            else:
                result.setNumerator(n1 + n2)
                result.setDenominator(d1)
                result = self.reduction(result)
        elif op == "-":
            if d1 != d2:
                n1 = n1 * d2
                n2 = n2 * d1
                d1 = d1 * d2
                d2 = d1
                result.setNumerator(n1 - n2)
                result.setDenominator(d1)
                result = self.reduction(result)
            else:
                result.setNumerator(n1 - n2)
                result.setDenominator(d1)
                result = self.reduction(result)
        elif op == "×":
            result.setNumerator(n1 * n2)
            result.setDenominator(d1 * d2)
            result = self.reduction(result)
        elif op == "÷":
            result.setNumerator(n1 * d2)
            result.setDenominator(d1 * n2)
            result = self.reduction(result)
        else:
            print("errorCaculation.py")
        return result
