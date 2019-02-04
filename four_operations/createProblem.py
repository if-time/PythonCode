# -*- coding: utf-8 -*-

import random
import datetime
import fraction
class create:
    def createOperator(self):
        operator = ["+", "-", "×", "÷"]
        n = random.randint(0, 3)
        return operator[n]

    def createArithmetic(self):
        list = []
        f1 = create()
        f2 = create()
        operator_no = random.randint(1, 3)
        if operator_no == 1:
            list.append(f1.createNum())
            list.append(f2.createOperator())
            list.append(f1.createNum())
        elif operator_no == 2:
            start = random.randint(0, 2)
            end = 0
            if start == 0:
                end == 0
            else:
                end = start + 1
            for i in range(1, 4):
                if i == start:
                    list.append("(")
                list.append(f1.createNum())
                if i == end:
                    list.append(")")
                list.append(f2.createOperator())
            list.pop()
        elif operator_no == 3:
            start = random.randint(0, 3)
            end = 0
            if start == 0:
                end == 0
            else:
                end = start + 1 + random.randint(0, 1)
                if end >= 4:
                    end = 4
            for i in range(1, 5):

                if i == start:
                    list.append("(")
                list.append(f1.createNum())
                if i == end:
                    list.append(")")
                list.append(f2.createOperator())
            list.pop()
        else:
            list.append(f1.createNum())
            list.append(f2.createOperator())
            list.append(f1.createNum())

        return list

    def toString(self, list):
        exp = ""
        for i in range(len(list)):
            if type(list[i]) == fraction.fraction:
                exp = exp + list[i].toString()
            else:
                exp = exp + str(list[i])
        return exp

        # 生成随机数
    def createNum(self):
        n = fraction.fraction()
        b = random.randint(1, 9)
        a = random.randint(1, b * 10 - 1)
        tmp = create()
        divisor = tmp.getMaxDivisor(a, b)
        a = a / divisor
        b = b / divisor
        n.setNumerator(a)
        n.setDenominator(b)
        return n

        # 约分
    def reduction(self, fraction):
        a = fraction.numerator
        b = fraction.denominator
        divisor = create.getMaxDivisor(a, b)
        a = a / divisor
        b = b / divisor
        fraction.setNumerator(a)
        fraction.setDenominator(b)
        return fraction

        # 求最大公约数
    def getMaxDivisor(self, numerator, denominator):
        tmp = create()
        if denominator == 0:
            return numerator
        else:
            x = numerator % denominator
            return tmp.getMaxDivisor(denominator, x)