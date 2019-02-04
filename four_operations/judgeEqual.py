# -*- coding: utf-8 -*-
from binaryTree import *
import random

class judge:

    def __init__(self):
        self.judge = []
        self.repeat_no = 0

    def translateSuffix(self, exp):
        right = []
        Stack = []
        position = 0
        while True:
            if self.isOperator(exp[position]):
                if exp == [] or exp[position] == "(":
                    Stack.append(exp[position])
                else:
                    if exp[position] == ")":
                        while True:
                            if Stack != [] and Stack[-1] != "(":
                                operator = Stack.pop()
                                right.append(operator)
                            else:
                                if Stack != []:
                                    Stack.pop()
                                break
                    else:
                        while True:
                            if Stack != [] and self.priority(exp[position], Stack[-1]):
                                operator = Stack.pop()
                                if operator != "(":
                                    right.append(operator)
                            else:
                                break
                        Stack.append(exp[position])
            else:
                right.append(exp[position])
            position = position + 1
            if position >= len(exp):
                break
        while Stack != []:
            operator = Stack.pop()
            if operator != "(":
                right.append(operator)
        return right

    def isOperator(self, operator):
        if operator == "+" or operator == "-" or operator == "×" or operator == "÷" or operator == "(" or operator == ")":
            return True
        else:
            return False

    def priority(self, operatorout, operatorin):
        m = -1
        n = -1
        addop = [["+", "-", "×", "÷", "(", ")"], ["+", "-", "×", "÷", "(", ")"]]
        first = [[1, 1, 2, 2, 2, 0], [1, 1, 2, 2, 2, 0],
                 [1, 1, 1, 1, 2, 0], [1, 1, 1, 1, 2, 0],
                 [2, 2, 2, 2, 2, 0], [2, 2, 2, 2, 2, 2]]
        for i in range(6):
            if operatorin == addop[0][i]:
                m = i
        for i in range(6):
            if operatorout == addop[1][i]:
                n = i
        if m == -1 and n == -1:
            return False
        elif m == -1 and n != -1:
            return False
        elif m != -1 and n == -1:
            return True
        elif first[m][n] == 1:
            return True
        else:
            return False

    def createTree(self, suffix):
        stacks = []
        for i in range(0, len(suffix)):
            tree = BinaryTree()
            ob = suffix[i]
            if self.isOperator(ob):
                t2 = BinaryTree()
                t1 = BinaryTree()
                t2 = stacks.pop()
                t1 = stacks.pop()
                if self.maxTree(t1, t2):
                    tree.setNumber(ob)
                    tree.setLeft(t1)
                    tree.setRight(t2)
                    tree.setValue(self.count(ob, t1.value, t2.value))
                else:
                    tree.setNumber(ob)
                    tree.setLeft(t2)
                    tree.setRight(t1)
                    tree.setValue(self.count(ob, t1.value, t2.value))
                stacks.append(tree)
            else:
                tree.setNumber(ob)
                tree.setValue(ob)
                stacks.append(tree)
        return tree

    def count(self, op, fraction1, fraction2):
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
            print("该字符不是操作符，错误位置：")
        return result

    def max(self, fraction1, fraction2):
        n1 = int(fraction1.numerator)
        d1 = int(fraction1.denominator)
        n2 = int(fraction2.numerator)
        d2 = int(fraction2.denominator)
        n1 = n1 * d2
        n2 = n2 * d1
        if n1 > n2:
            return 1
        elif n1 < n2:
            return 2
        else:
            return 3

#生成随机数

    def createNum(self):
        n = fraction.fraction()
        b = random.randint(1,9)
        a = random.randint(1,b*10-1)
        divisor = self.getMaxDivisor(a,b)
        a = a/divisor
        b = b/divisor
        n.setNumerator(a)
        n.setDenominator(b)
        return n

    #约分
    def reduction(self,fraction):
        a = fraction.numerator
        b = fraction.denominator
        divisor = self.getMaxDivisor(a, b)
        a = a / divisor
        b = b / divisor
        fraction.setNumerator(a)
        fraction.setDenominator(b)
        return fraction

    #求最大公约数
    def getMaxDivisor(self,numerator,denominator) :
        if denominator == 0:
            return numerator
        else:
            x = numerator%denominator
            return self.getMaxDivisor(denominator, x)

    def maxTree(self, t1, t2):
        max = self.max(t1.value, t2.value)
        if max == 1:
            return True
        elif max == 2:
            return False
        elif self.priority(t1.number, t2.number):
            if t1.left == None or t2.left == None:
                return True
            max = self.max(t1.left.value, t2.left.value)
            if max == 1:
                return True
            elif max == 2:
                return False
            else:
                return True
        return False