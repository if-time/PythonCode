#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

    for x, y in data.items():
    	print("{} uses {}".format(x, y))


#!/usr/bin/env python3
n = int(input("Enter the number of students: "))
data = {} # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History') # 所有科目
for i in range(0, n):
    name = input('Enter the name of the student {}: '.format(i + 1)) # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科的分数
    data[name] = marks
for x, y in data.items():
    total =  sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")



#!/usr/bin/env python3
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)  


#如果你想要分几行输入字符串，并且希望行尾的换行符自动包含到字符串当中，
#可以使用三对引号："""...""" 或 '''...''' 。

#回文检测
#!/usr/bin/env python3
s = input("Please enter a string: ")
z = s[::-1]
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")



#!/usr/bin/env python3
s = input("Please enter a string: ")
z = s[::-1]
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


#[:-1]表示字符串的最后一个元素。
#实际写法是s[0:-1],s[0]是第一个元素，s[0：3]实际是表示s[0] s[1] s[2] ，
#所以s[-1]就是表示去掉最后一个元素后的所有元素。

#!/usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print("Oh no")


#有两个非常重要的地方，第一个是具有默认值的参数后面不能再有普通参数，比如 f(a,b=90,c) 就是错误的。

#第二个是默认值只被赋值一次，因此如果默认值是任何可变对象时会有所不同，比如列表、字典或大多数类的实例。
#例如，下面的函数在后续调用过程中会累积（前面）传给它的参数:

def f(a, data=[]):
     data.append(a)
     return data

print(f(1))
#[1]
print(f(2))
#[1, 2]
print(f(3))
#[1, 2, 3]

#要避免这个问题，你可以像下面这样：

def f(a, data=None):
    if data is None:
        data = []
    data.append(a)
    return data

print(f(1))
#[1]
print(f(2))
#[2]



#!/usr/bin/env python3

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())


#多继承
class MyClass(Parentclass1, Parentclass2):
	def __init__(self):
		Parentclass1.__init__(self)
		Parentclass2.__init__(self)






#你可能想要更精确的调整控制属性访问权限，你可以使用 @property 装饰器，@property 装饰器就是负责把一个方法变成属性调用的。

#下面有个银行账号的例子，我们要确保没人能设置金额为负，并且有个只读属性 cny 返回换算人名币后的金额。



#!/usr/bin/env python3

class Account(object):
    """账号类,
    amount 是美元金额.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """账号余额（美元）"""
        return self.__amt

    @property
    def cny(self):
        """账号余额（人名币）"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=6.6) # 基于课程编写时的汇率
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -100
    print("Dollar amount:", acc.amount)

#运行程序：
#Dollar amount: 20
#In CNY: 132.0
#Sorry, no negative amount in the account.
#Dollar amount: 20
#此处输入图片的描述



#Requests 是一个第三方 Python 模块，其官网的介绍如下：

#Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用。

#警告：非专业使用其他 HTTP 库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。

#第三方模块并不是默认的模块，意味着你需要安装它，我们使用 pip3 安装它。

#首先要安装 pip3：

# $ sudo apt-get update
# $ sudo apt-get install python3-pip
#然后用 pip3 安装 requests

# $ sudo pip3 install requests
#上面的命令会在你的系统中安装 Python3 版本的 Requests 模块。

#4.2.1 获得一个简单的网页
#你可以使用 get() 方法获取任意一个网页。

#>>> import requests
#>>> req = requests.get('https://github.com')
#>>> req.status_code
#200
#req 的 text 属性存有服务器返回的 HTML 网页，由于 HTML 文本太长就不在这里贴出来了。

#使用这个知识，让我们写一个能够从指定的 URL 中下载文件的程序。

#代码写入文件 /home/shiyanlou/download.py：

#!/usr/bin/env python3
import os
import os.path
import requests

def download(url):
    '''从指定的 URL 中下载文件并存储到当前目录

    :arg url: 要下载的文件的 URL
    '''
    req = requests.get(url)
    # 首先我们检查是否存在文件
    if req.status_code == 404:
        print('No such file found at %s' % url)
        return
    filename = url.split('/')[-1]
    with open(filename, 'wb') as fobj:
        fobj.write(req.content)
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)

"""
#测试一下程序：
shiyanlou:~/ $ chmod +x *.py                                                    [10:26:52]
shiyanlou:~/ $ ./download.py                                                    [10:26:58]
Enter a URL: http://labfile.oss.aliyuncs.com/courses/596/sample.txt
Download over.
shiyanlou:~/ $ ll                                                               [10:27:46]
\u603b\u7528\u91cf 28K
-rwxrwxr-x 1 shiyanlou shiyanlou  380  7\u6708 15 09:47 bars.py
drwxrwxr-x 2 shiyanlou shiyanlou 4.0K  8\u6708 17  2016 Code
drwxrwxr-x 2 shiyanlou shiyanlou 4.0K  8\u6708 17  2016 Desktop
-rwxrwxr-x 1 shiyanlou shiyanlou  424  7\u6708 15 10:26 download.py
-rwxrwxr-x 1 shiyanlou shiyanlou    0  7\u6708 15 10:21 downlod.py
drwxrwxr-x 2 shiyanlou shiyanlou 4.0K  7\u6708 15 09:56 mymodule
drwxrwxr-x 2 shiyanlou shiyanlou 4.0K  7\u6708 15 09:48 __pycache__
-rw-rw-r-- 1 shiyanlou shiyanlou   33  7\u6708 15 10:27 sample.txt


可以看到目录下已经多了一个 sample.txt 文件。

你可能已经注意到了 if __name__ == '__main__': 这条语句，
它的作用是，只有在当前模块名为 __main__ 的时候（即作为脚本执行的时候）才会执行此 if 块内的语句。
换句话说，当此文件以模块的形式导入到其它文件中时，if 块内的语句并不会执行。

你可以将上面的程序修改的更友好些。举个例子，你可以检查当前目录是否已存在相同的文件名。os.path 模块可以帮助你完成这个。
"""


"""
改写我们在第11节类这个模块当中 2.3 继承 部分的 student_teacher.py 脚本，
在Person()类中增添函数get_grade()。对于教师类，
该函数可以自动统计出老师班上学生的得分情况并按照频率的高低以A: X, B: X, C: X, D: X 的形式打印出来。
对于学生类，该函数则可以以Pass: X, Fail: X 来统计自己的成绩情况（A,B,C 为 Pass, 如果得了 D 就认为是 Fail）。
"""

#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    \u8fd4\u56de\u5177\u6709\u7ed9\u5b9a\u540d\u79f0\u7684 Person \u5bf9\u8c61
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        \u8fd4\u56de\u5305\u542b\u4eba\u540d\u7684\u5b57\u7b26\u4e32
        """
        return self.name

    def get_grade(self):
        return self.grade


class Student(Person):
    """
    \u8fd4\u56de Student \u5bf9\u8c61\uff0c\u91c7\u7528 name, branch, year 3 \u4e2a\u53c2\u6570
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name, grade)
        self.branch = branch
        self.year = year
                                                   
    def get_details(self):
        """
        \u8fd4\u56de\u5305\u542b\u5b66\u751f\u5177\u4f53\u4fe1\u606f\u7684\u5b57\u7b26\u4e32
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        c = Counter(self.grade)
        p = c['A'] + c['B'] + c['C']
        f = c['D']
        return "Pass: {}, Fail: {}".format(p, f)


class Teacher(Person):
    """
    \u8fd4\u56de Teacher \u5bf9\u8c61\uff0c\u91c7\u7528\u5b57\u7b26\u4e32\u5217\u8868\u4f5c\u4e3a\u53c2\u6570
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name, grade)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        m = Counter(self.grade).most_common()
        s = ["{}: {}".format(x, y) for x, y in m]
        return ','.join(s)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Wrong!!")
        sys.exit(1)
    if sys.argv[1] == 'teacher':
        t = Teacher('Kane', 'English', sys.argv[2])
        print(t.get_grade())
    else:
        s = Student('ddd', 'English', 2016, sys.argv[2])
        print(s.get_grade())

#person1 = Person('Sachin')
#student1 = Student('Kushal', 'CSE', 2005)
#teacher1 = Teacher('Prashad', ['C', 'C++'])

#print(person1.get_details())
#print(student1.get_details())
#print(teacher1.get_details())


"""
__iter__()，返回迭代器对象自身。这用在 for 和 in 语句中。

__next__()，返回迭代器的下一个值。如果没有下一个值可以返回，那么应该抛出 StopIteration 异常。
"""

class Counter(object):
     def __init__(self, low, high):
         self.current = low
         self.high = high

     def __iter__(self):
         return self

     def __next__(self):
     	#返回下一个值直到当前值大于 high
         if self.current > self.high:
             raise StopIteration
         else:
             self.current += 1
             return self.current - 1
 
c = Counter(5, 10)
for i in c:
     print(i, end=' ')
 
# 5 6 7 8 9 10  

# 我们已经看过在 for 循环中使用迭代器的例子了，下面的例子试图展示迭代器被隐藏的细节：

iterator = iter(c)
while True:
     try:
         x = iterator.__next__()
         print(x, end=' ')
     except StopIteration as e:
         break

# 5 6 7 8 9 10

"""
在这一节我们学习有关 Python 生成器（Generators）的知识。
生成器是更简单的创建迭代器的方法，这通过在函数中使用 yield 关键字完成：
"""

def my_generator():
     print("Inside my generator")
     yield 'a'
     yield 'b'
     yield 'c'

my_generator()
# <generator object my_generator at 0x7fbcfa0a6aa0>
"""
在上面的例子中我们使用 yield 语句创建了一个简单的生成器。
我们能在 for 循环中使用它，就像我们使用任何其它迭代器一样。

for char in my_generator():
     print(char)

Inside my generator
a
b
c
"""

"""
在下一个例子里，我们会使用一个生成器函数完成与 Counter 类相同的功能，并且把它用在 for 循环中。
"""
def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1
 
for i in counter_generator(5,10):
    print(i, end=' ')
 
# 5 6 7 8 9 10

def infinite_generator(start=0):
    while True:
        yield start
        start += 1

for num in infinite_generator(4):
    print(num, end=' ')
    if num > 20:
        break

# 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

# 我们会发现生成器的一个特点：它们是不可重复使用的。
# 一个创建可重复使用生成器的方式是不保存任何状态的基于对象的生成器。
# 任何一个生成数据的含有 __iter__ 方法的类都可以用作对象生成器。

class Counter(object):
    def __init__(self, low, high):
         self.low = low
         self.high = high
    def __iter__(self):
         counter = self.low
         while self.high >= counter:
             yield counter
             counter += 1

gobj = Counter(5, 10)
for num in gobj:
    print(num, end=' ')

# 5 6 7 8 9 10

for num in gobj:
    print(num, end=' ')

# 5 6 7 8 9 10

"""
上面的 gobj 并不是生成器或迭代器，因为它不具有 __next__ 方法，
只是一个可迭代对象，生成器是一定不能重复循环的。
如果想要使类的实例变成迭代器，可以用 __iter__ + __next__ 方法实现：
"""

from collections import Iterator
class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        self.a += 1
        if self.a > self.b:
            raise StopIteration()
        return self.a
     

test = Test(5, 10)

isinstance(test, Iterator)
True

# 闭包（Closures）是由另外一个函数返回的函数。我们使用闭包去除重复代码。
def add_number(num):
    def adder(number):
        #adder 是一个闭包
        return num + number
    return adder

a_10 = add_number(10)
a_10(21)
# 31
a_10(34)
# 44
a_5 = add_number(5)
a_5(3)
# 8


# 装饰器（Decorators）用来给一些对象动态的添加一些新的行为，我们使用过的闭包也是这样的。
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    #我们的求和函数
    return a + b

add(1, 3)
"""
Before call
After call
4
"""


"""
assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(x)	bool(x) is True
assertFalse(x)
assertIs(x) a is b
assertIsNone(x)
assertIn(a, b)	a in b
assertIsInstance(a, b) isinstance(a, b)
"""

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
	# 显示用户的名称
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
	return 'Post %d' % post_id
	


from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


"""
/
/login
/login?next=%2F
/user/John%20Doe
"""

from flask import request 
from flask import render_template                    
from flask import Flask   
                      
app = Flask(__name__)     
                      
@app.route('/login', method=['POST', 'GET'])         
def login():        
    error = None    
    if request.method == 'POST':                     
        if valid_login(request.form['username'],    
                       request.form['password']):    
            return log_the_user_in(request.form['username'])
        else:       
            error = 'Invalid username/passeord'      
 # \u5f53\u8bf7\u6c42\u5f62\u5f0f\u4e3a\u2018GET\u2019\u6216\u8005\u8ba4\u8bc1\u5931\u8d25\u5219\u6267\u884c\u4ee5\u4e0b\u4ee3\u7801    
    return render_template('logim.html', error=error)
                   
if __name__ == '__main__':
    app.run()       
    app.debug = True     



# 上传的文件是存储在内存或者文件系统上一个临时位置。你可以通过请求对象中files属性访问这些文件。
# 每个上传的文件都会存储在这个属性字典里。它表现得像一个标准的 Python file对象，
# 但是它同样具有save()方法，该方法允许你存储文件在服务器的文件系统上。

# 下面是一个简单的例子用来演示提交文件到服务器上:

from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    
# 如果你想要知道在上传到你的应用之前在客户端的文件名称，你可以访问filename属性。
# 但请记住永远不要信任这个值，因为这个值可以伪造。
# 如果你想要使用客户端的文件名来在服务器上存储文件，把它传递到Werkzeug提供给你的secure_filename()函数:

from flask import request
from werkzeug import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    

import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/upload',methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html',filename=file.filename)
        else:
            return render_template('upload.html',error="file:\""+file.filename+"\" is not in "+_filter(str(list(ALLOWED_EXTENSIONS))))
    else:
        err = 'upload is error'
    return render_template('upload.html',error="Welcome")
def allowed_file(filename):
    "判断上传文件格式并返回判断结果(True/False)"
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def _filter(str):
    "过滤集合中的指定字符"
    dirty_stuff = ["'", "[","]"]
    for stuff in dirty_stuff:
        str = str.replace(stuff, "")
    return str


# 列表切片的形式是：list[起始索引：终止索引（不包含）：步长间隔]
