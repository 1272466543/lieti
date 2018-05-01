
class Student():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.setName(name)
	def intro(self):
		print("Hai,my name is {0}".format(self.name))
	def setName(self,name):
		self.name = name.upper()  #upper()转变为大写
s1 = Student("LIU Ying",19)
s2 = Student("alex max",24)
s1.intro()
s2.intro()

print("*" * 20)
class Person():
	
	#说明文档写在这里

	def fget(self):
		return self._name * 2
	def fset(self,name):
		self._name = name.upper()
	def fdel(self):
		self._name = "NoName"
	name = property(fget,fset,fdel,"对name进行下操作")
p1 = Person()
p1.name = "TuLing"
print(p1.name)

'''
__dict__以字典的方式显示累的成员组成
__doc__获取类的文档信息
__name__获取类的名称，如果在模块中使用，获取模块的名称
__bases__获取某个类的所有父类，以元组的方式显示
'''



#__init__ 构造函数
'''
class A():
	def __init__(sel,name = 0):
		print("哈哈 我被调用了")
a = A()
'''

#__new__  对象实例化方法，此函数比较特殊 一般不需要使用
#__call__  对象当函数使用的时候触发
'''
class A():
	def __init__(sel,name = 0):
		print("哈哈 我被调用了")
	def __call__(self):
		print("我又被调用了")
a = A()
a()
'''
#__str__ 当对象被当做字符串的时候调用
'''
class A():
	def __init__(sel,name = 0):
		print("哈哈 我被调用了")
	def __call__(self):
		print("我又被调用了")
	def __str__(self):
		return "例子"
a = A()
print(a)
'''
#__repr__  返回字符串 与__str__的区别请百度

'''
class A():
	name = "NoName"
	age = 18
	def __getattr__(self,name):  #__getattr__访问一个不存在的属性时触发
		print("没找到")
		print(name)
a = A()
print(a.name)





print(a.addr)
'''
#__setattr__ 对成员属性进行设置的时候触发   在该方法中不能对属性直接进行赋值操作 否则死循环
'''
class Person():
	def __init__(self):
		pass
	def __setattr__(self,name,value):
		print("设置属性：{0}".format(name))
		#下面语句会导致死循环
		#self.name = value
		#为了避免死循环，统一调用父类魔法函数
		super().__setattr__(name,value)
p = Person()
print(p.__dict__)
p.age = 18
'''
#__gt__进行大于判断的时候触发的函数
'''
class Student():
	def __init__(self,name):
		self._name = name
	def __gt__(self,obj):
		print("哈哈 {0}会比{1}大么".format(self,obj))
		return self._name > obj._name
stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)
'''

'''
#三种方法案例
class Person():
	#实例方法
	def eat(self):
		print(self)
		print("Eating.....")
	#类方法  第一个参数一般为cls  区别于self
	def play(cls):
		print(cls)
		print("Playing.....")
	#静态方法 不需要用第一个参数表示自身或者类
	def say():
		print("Saying......")
yueyue = Person()
#实例方法
yueyue.eat()
#类方法
Person.play()
yueyue.play()

#静态方法
Person.say()
yueyue.say()
'''
#???????????????????????????????????????????????????????




'''
class A():
	def __init__(self):
		self.name = "haha"
		self.age = 18
	def fget(self):
		print("我被读取了")
		return self.name
	def fset(self,name):
		print("我被写入了，但是还可以做好多事情")
		self.name = "tul" + name
	def fdel(self):
		pass
	name2 = property(fget,fset,fdel,"这是一个例子")
a = A()
#print(a.name)
print(a.name2)

'''


#定义抽象类要调用 import ABC  

'''
from types import MethodType
class A():
	pass
def say(self):
	print("Saying...")
a = A()
a.say = MethodType(say,A)  #把say当成方法类型来使用
a.say()
'''

#利用type来造一个类

#先定义类应该具有的成员函数
def say(self):
	print("Saying...")
def talk(self):
	print("Talking...")
#用type来创建一个类
A = type("AName",(object,),{"class_say":say,"class_talk":talk})
#然后可以像正常访问一样使用类
a = A()
#??????????????????????????????????????

#元类—— MetaClass  它是一个类  备用来创造别的类
#它的写法是固定的，塔必须继承与type
#一般以MetaClass结尾
class TulingMetaClass(type):
	def __new__(cls,name,bases,attrs):
		print("sdadad")
		attrs['id'] = '000000'
		attrs['addr'] = "sdad2wdqqwddqw"
		return type.__new__(cls,name,bases,attrs)
#元类定义完就可以使用，
class Teacher(object,metaclass=TulingMetaClass):
	pass
t = Teacher()
t.__dict__
t.id