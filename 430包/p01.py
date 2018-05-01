class Student():
	def __init__(self,name = "NoName",age = 18):
		self.name = name
		self.age = age
	def say(self):
		print("My name is {0}".format(self.name))
def sayHello():
	print("Hi  欢迎来到这")

if __name__ == '__main__':  #有效避免模块代码被导入的时候被动执行的问题
	print("我是p01")
'''
模块导入 import module_name
		module_name.function_name
		module_name.class_name
'''
