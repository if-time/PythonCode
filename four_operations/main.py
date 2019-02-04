# -*- coding: utf-8 -*-
import createProblem
import judgeEqual
import binaryTree

class Main(object):

    def createProblem(self, problemNumber):
        createPro = createProblem.create()
        file = open("Exercises.txt", "w")
        file2 = open("Answer.txt","w")
        hashList = []
        count = 0
        while count < problemNumber:
            problemList = []
            formula = createPro.createArithmetic()
            k = judgeEqual.judge()
            tree = k.createTree(k.translateSuffix(formula))
            btree = binaryTree.binaryTree()
            problemList = btree.outPutTree(tree, problemList)
            newproblem = ''
            for st in problemList:
                if st in ['`', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '×', '÷']:
                    newproblem += st
            m = hash(newproblem)
            if m not in hashList:
                hashList.append(m)
                count += 1
                file.write(createPro.toString(formula) + '\n')
                file2.write(str(tree.value.toString())+'\n')
            else:
                continue
        file.close()
        file2.close()

    def sloveProblem(self, pathProblem, pathAnswer):
        fPro = open(pathProblem, "r")
        fAns = open(pathAnswer, "r")
        problemList = []
        ansList = []
        caculateAnsList = []
        for index, line in enumerate(fPro.readlines()):
            problemList.append(line.strip())
            k = judgeEqual.judge()
            tree = k.createTree(k.translateSuffix(list))
            caculateAnsList.append(str(tree.value.toString()))

        for index, line in enumerate(fAns.readlines()):
            ansList.append(line.strip())

    def judgeEqual(self, ansList, caculateAnsList):
        count = 0
        ansLen = len(ansList)
        wrongAns = []
        rightAns = []
        while count < ansLen:
            if ansList[count] != caculateAnsList[count]:
                wrongAns.append(int(count) + 1)
            else:
                rightAns.append(int(count) + 1)
        f = open("Grade.txt","w")
        f.write("错误题号:")
        count = 0
        while count < len(wrongAns):
            f.write(wrongAns[count])
            count += 1
        f.write('\n')
        count = 0
        f.write("正确题号：")
        while count < len(rightAns):
            f.write(rightAns[count])
            count += 1

if __name__ == "__main__":
    tmp = Main()
    while True:
        print('1.生成题目和答案\n2.解题\n3.退出\n')
        option = input()
        if option == '1':
            print('请输入需要生成题目的数量：')
            problemNumber = input()

            tmp.createProblem(int(problemNumber))
        elif option == '2':
            print('请输入完整题目文件名（如:1.txt）:')
            fileNamePro = input()
            print('请输入完整答案文件名：')
            fileNameAns = input()
            tmp.sloveProblem(fileNamePro, fileNameAns)
        elif option == '3':
            break
        else:
            print('请输入正确的编号')
