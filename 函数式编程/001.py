#lambda表达式的用法
#1.以lambda开头
#2.紧跟一定的参数(如果有的话)
#3.参数后面用冒号和表达式主题隔开
#4.只是一个表达式 没有return
'''
stm = lambda x: 100 * x
print(stm(89))

stm2 = lambda x,y,z: x+y*10+z*100
print(stm2(4,5,6))
#变量可以赋值
#函数名称是变量

l1 = [i for i in range(1,10)]
print(l1)
l2 = []
for i in l1:
	l2.append(i * 10)
print(l2)
##############################
def mulTen(n):
	return n * 10
l3 = map(mulTen,l1)
#map类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
	print(i)
################################
#reduce 需要导入functools包   必须有两个参数，必须有返回结果
#把一个可迭代对象最后归并成一个结果
#reduce([1,2,3,4,5]) == f(f(f(f(1,2),3),4),5)
from functools import reduce
def myAdd(x,y):
	return x + y
rst = reduce(myAdd,[1,2,3,4,5,6,])
print(rst)
'''
##########################
#map会生成一个跟原来数据相对应得新队列
#filter不一定，只有符合条件的才会进入新的数据集合
#利用给定函数进行判断 返回值一定是一个布尔值
#调用格式：filter(f,data),f是过滤函数，data是数据
'''
def isEven(a):
	return a % 2 == 0
l = [1,545,4,5,4,5,4,4,544,5,4,45,45,6,89,74,1,3,5,4]
rst = filter(isEven,l)
print(type(rst))
#返回的filter是一个可迭代对象
print(rst)
print([i for i in rst])
'''
##############################
'''
#排序
a = [2,5645,546,21,4,84,7]
al = sorted(a,reverse=True)
print(al)


a = [2,-8,-96,54,85,44554,7887,56]
#abs是求绝对值额意思 即按照绝对值的倒叙排列
al = sorted(a,key=abs,reverse=True)
print(al)


def myF4(*args):
	def myF5():
		rst = 0
		for n in args:
			rst += n
		return rst
	return myF5
f5 = myF4(1,2,3,4,5,6,7,8,9,0)
print(f5())

def count():

	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1,f2,f3 = count()
print(f1())

def count2():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())
'''
'''
import time
def printTime(f):
	def wrapper(*args, **kwargs):
		print("Time:",time.ctime())
		return f(*args, **kwargs)
	return wrapper
#上面定义了装饰器，使用的时候要用到@
@printTime
def Hello():
	print("Hello world")
Hello()

#装饰器的好处是，一旦定义则可以装饰任意函数
#上面对函数的装饰使用了系统定义的语法糖
#下面开始手动执行下装饰器

def hello3():
	print("hhhhhhhh")
hello3()
hello3 = printTime(hello3)
hello3()

f = printTime(hello3)
f()
'''
def int16(x,base=16):
	return int(x,base)

print(int16("12345"))


int("12345")
print(int("12345",base=8))
#偏函数  实现上面int16的功能
import functools
int16 = functools.partial(int,base=16)
print(int16("12345"))