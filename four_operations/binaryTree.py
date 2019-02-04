# -*- coding: utf-8 -*-
import fraction


class BinaryTree(object):

    def __init__(self):
        self.number = None
        self.left = None
        self.right = None
        self.value = None

    def tree(self, number, left, right, value):
        self.number = number
        self.left = left
        self.right = right
        self.value = value

    def setNumber(self, number):
        self.number = number

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setValue(self, value):
        self.value = value

    def toString(self, tree):
        s = ""
        s = self.outPutTree(tree, s)
        return s

    def outPutTree(self, tree, s):
        if tree is None:
            s1 = self.outPutTree(tree.left, s)
            s2 = self.outPutTree(tree.right, s)

            if type(tree.number) == fraction.num:
                return str(s1) + str(s2) + str(tree.number.toString())
            else:
                return str(s1) + str(s2) + str(tree.number)
        return s

    def createTree(self, exp):
        stack = []
        op = ['+','-','×','÷']
        for i in exp:
            if i not in op:
                tree = BinaryTree(int(i))
                stack.append(tree)
