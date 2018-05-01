
class Person():
	name = "NoName"
	age = 0
	__score = 0#只能自己知道
	_petname = "sec"#子类可用不能共用
	def sleep(self):
		print("Sleeping...")
	def work(self):
		print("make some money")
#父类写在括号内
class Teacher(Person):
	tecaher_id = "9527"
	name = "DaNa"
	def make_test(self):
		print("attention")
	def work(self):
		#super代表得到父类
		super().work()
		#Person.work(self)
		self.make_test()
t = Teacher()
t.work()

print("*"*20)
#迭代器 生成器 装饰器。。。。。。。。。。。。。。。。。。。。。。。

class A():
	def __init__(self):
		print("A")
class B(A):
	def __init__(self,name):
		print("B")
		print(name)
class C(B):
	def __init__(self,name):
		B.__init__(self,name)
		print("这就是C中的附加功能")
c = C("我是C")

print("*************************************")
class Person():
	name = "liuying"
	age = 18

	def eat(self):
		print("EAT......")
	def drink(self):
		print("DRINK......")
	def sleep(self):
		print("SLEEP......")
class Teacher(Person):
	def work(self):
		print("Work")
class Student(Person):
	def study(self):
		print("Study")
class Tutor(Teacher,Student):
	pass
t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__) 

'''
class A():
	name = "lx"
class B(A):
	pass
class C():
	pass
print(issubclass(B,A))

a = A()
print(isinstance(a,A))  #检测一个类是否是另一个类的子类
print(hasattr(a,"name")) #检测一个对象是否是另一个类的实例
help(setattr)
#dir  获取成员列表
'''