#encoding=utf-8
import random
from fractions import Fraction

def newint(encoding='utf-8'):
    opr = ['+', '-', '*', '/']
    fh1 = random.choice(opr)
    fh2 = random.choice(opr)
    fh3 = random.choice(opr)
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    n3 = random.randint(1, 20)
    n4 = random.randint(1, 20)
    rjg = 0
    if fh1 == '+':
      if fh2 == '+':
        if fh3 == '+':
          rjg = n1+n2+n3+n4
        elif fh3 == '-':
          rjg = n1+n2+n3-n4
        elif fh3 == '*':
          rjg = n1+n2+n3*n4
        elif fh3 == '/':
          rjg = n1+n2+n3/n4
      elif fh2 == '-':
        if fh3 == '+':
          rjg = n1+n2-n3+n4
        elif fh3 == '-':
          rjg = n1+n2-n3-n4
        elif fh3 == '*':
          rjg = n1+n2-n3*n4
        elif fh3 == '/':
          rjg = n1+n2-n3/n4
      elif fh2 == '*':
        if fh3 == '+':
          rjg = n1+n2*n3+n4
        elif fh3 == '-':
          rjg = n1+n2*n3-n4
        elif fh3 == '*':
          rjg = n1+n2*n3*n4
        elif fh3 == '/':
          rjg = n1+n2*n3/n4
      elif fh2 == '/':
        if fh3 == '+':
          rjg = n1+n2/n3+n4
        elif fh3 == '-':
          rjg = n1+n2/n3-n4
        elif fh3 == '*':
          rjg = n1+n2/n3*n4
        elif fh3 == '/':
          rjg = n1+n2/n3/n4
    elif fh1 == '-':
      if fh2 == '+':
        if fh3 == '+':
          rjg = n1-n2+n3+n4
        elif fh3 == '-':
          rjg = n1-n2+n3-n4
        elif fh3 == '*':
          rjg = n1-n2+n3*n4
        elif fh3 == '/':
          rjg = n1-n2+n3/n4
      elif fh2 == '-':
        if fh3 == '+':
          rjg = n1-n2-n3+n4
        elif fh3 == '-':
          rjg = n1-n2-n3-n4
        elif fh3 == '*':
          rjg = n1-n2-n3*n4
        elif fh3 == '/':
          rjg = n1-n2-n3/n4
      elif fh2 == '*':
        if fh3 == '+':
          rjg = n1-n2*n3+n4
        elif fh3 == '-':
          rjg = n1-n2*n3-n4
        elif fh3 == '*':
          rjg = n1-n2*n3*n4
        elif fh3 == '/':
          rjg = n1-n2*n3/n4
      elif fh2 == '/':
        if fh3 == '+':
          rjg = n1-n2/n3+n4
        elif fh3 == '-':
          rjg = n1-n2/n3-n4
        elif fh3 == '*':
          rjg = n1-n2/n3*n4
        elif fh3 == '/':
          rjg = n1-n2/n3/n4
    elif fh1 == '*':
      if fh2 == '+':
        if fh3 == '+':
          rjg = n1*n2+n3+n4
        elif fh3 == '-':
          rjg = n1*n2+n3-n4
        elif fh3 == '*':
          rjg = n1*n2+n3*n4
        elif fh3 == '/':
          rjg = n1*n2+n3/n4
      elif fh2 == '-':
        if fh3 == '+':
          rjg = n1*n2-n3+n4
        elif fh3 == '-':
          rjg = n1*n2-n3-n4
        elif fh3 == '*':
          rjg = n1*n2-n3*n4
        elif fh3 == '/':
          rjg = n1*n2-n3/n4
      elif fh2 == '*':
        if fh3 == '+':
          rjg = n1*n2*n3+n4
        elif fh3 == '-':
          rjg = n1*n2*n3-n4
        elif fh3 == '*':
          rjg = n1*n2*n3*n4
        elif fh3 == '/':
          rjg = n1*n2*n3/n4
      elif fh2 == '/':
        if fh3 == '+':
          rjg = n1*n2/n3+n4
        elif fh3 == '-':
          rjg = n1*n2/n3-n4
        elif fh3 == '*':
          rjg = n1*n2/n3*n4
        elif fh3 == '/':
          rjg = n1*n2/n3/n4
    elif fh1 == '/':
      if fh2 == '+':
        if fh3 == '+':
          rjg = n1/n2+n3+n4
        elif fh3 == '-':
          rjg = n1/n2+n3-n4
        elif fh3 == '*':
          rjg = n1/n2+n3*n4
        elif fh3 == '/':
          rjg = n1/n2+n3/n4
      elif fh2 == '-':
        if fh3 == '+':
          rjg = n1/n2-n3+n4
        elif fh3 == '-':
          rjg = n1/n2-n3-n4
        elif fh3 == '*':
          rjg = n1/n2-n3*n4
        elif fh3 == '/':
          rjg = n1/n2-n3/n4
      elif fh2 == '*':
        if fh3 == '+':
          rjg = n1/n2*n3+n4
        elif fh3 == '-':
          rjg = n1/n2*n3-n4
        elif fh3 == '*':
          rjg = n1/n2*n3*n4
        elif fh3 == '/':
          rjg = n1/n2*n3/n4
      elif fh2 == '/':
        if fh3 == '+':
          rjg = n1/n2/n3+n4
        elif fh3 == '-':
          rjg = n1/n2/n3-n4
        elif fh3 == '*':
          rjg = n1/n2/n3*n4
        elif fh3 == '/':
          rjg = n1/n2/n3/n4
    print(n1, opr[1], n2,opr[2] ,n3 ,opr[3], n4 ,'= ', end='')
    return rjg
    '''jg = input(encoding='utf-8')
    sr = int(jg)
    if int(sr) == rjg:
        print('right')
    else:
        print('error. the Tight answer is', rjg)'''

def newfra(encoding='utf-8'):
    opr = ['+', '-', '×', '÷']
    fh = random.randint(0, 3)
    t1 = random.randint(1, 10)
    t2 = random.randint(t1, 10)
    n1 = Fraction(t1, t2)
    t1 = random.randint(1, 10)
    t2 = random.randint(t1, 10)
    n2 = Fraction(t1, t2)
    rjg = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 / n2
    print(n1, opr[fh], n2, '= ', end='')
    return rjg
    '''jg = input()
    sr = Fraction(jg)
    if sr == rjg:
        print('right')
    else:
        print('error. the Tight answer is', rjg)'''

def newtest(encoding='utf-8'):
    opr = ['＋', '－', '×', '÷']
    print('输入题库所需要的题目数量')
    n=int(input())
    rjg=[]
    m=0
    while m<=(n-1):
        fh = random.randint(0, 4)
        if fh==0:
            print(m+1,end='、')
            rjg.append(newfra())
            print(' ')
        else:
            print(m+1,end='、')
            rjg.append(newint())
            print(' ')
        m=m+1
    m=0
    print('答案：')
    while m<=(n-1):
        print(m+1,'、',rjg[m])
        m=m+1
print('1、四则运算')
print('2、制作题库')
n=int(input())
if n==1:
    print('input "0000" to Quit')
    while True:
        fh = random.randint(0, 4)
        if fh == 0:
            rjg = newfra()
            jg = input()
            if jg == '0000':
                break;
            sr = Fraction(jg)
            if sr == rjg:
                print('right')
            else:
                print('error. the Tight answer is', rjg)
        else:
            rjg = newint()
            jg = input()
            if jg == '0000':
                break;
            sr = int(jg)
            if sr == rjg:
                print('right')
            else:
                print('error. the Tight answer is', rjg)
if n==2:
    newtest()
