
def stu(**kwargs):
	print("大家好，我先自我介绍一下：")
	print(type(kwargs))
	for k,v in kwargs.items():
		print(k,":",v)
	print("*"*10)
stu(name="lx",age=20,addr="shurendax",work="student")




def  stu(name,age,*args,hobby="没有",**kwargs):
	print("我叫{0}，我今年{1}岁了".format(name,age))
	if hobby=="没有":
		print("我没有爱好")
	else:
		print("我的爱好是{0}".format(hobby))
	print("*"*10)
	for i in args:
		print(i)
	print("#"*20)
	for k,v in kwargs.items():
		print(k,":",v)
name="lx"
age=18
stu(name,age)

stu(name,age,"lx0","lx1",hobby="游泳",hobby2="peng",hobby3="wan")
