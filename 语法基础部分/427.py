
class Student():
	name = "dana"
	age = 18
	def say(self):
		self.name = "aaaa"
		self.age = 200
		print("My name is {0}".format(self.name))
		print("My age is {0}".format(self.age))
	def sayAgain(s):
		print("My name is {0}".format(s.name))
		print("My age is {0}".format(s.age))

yueyue = Student()
yueyue.say()
yueyue.sayAgain()
###############################
print("***********************************")




class A():
	name = "liuying"
	age = 18
	def __init__(self):
		self.name = "aaa"
		self.age = "200"
	def say(self):
		print(self.name)
		print(self.age)
class B():
	name = "bbb"
	age = 90
a = A()
#a.say()

#A.say(a)
A.say(A)
#A.say(B)
#########################
'''
封装的三个级别：
	- 公开：public
	- 受保护的：protected
	- 私有的：private
私有成员是最高级别的封装 加两个下划线

'''