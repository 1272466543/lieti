#ramove移除指定的值，直接改变原有值，如果要删除的值不存在，报错
#discard移除集合中指定的值，跟ramove一样，但是如果要删除的话不报错
#add添加一个元素
#pop随机移除一个元素
#intersection交集
#differen差集
#union并集
#issubset检查一个集合是否为一个子集
#issuperset检查一个集合是否为超集
#frozen set冰冻集合，不可以进行任何修改的集合
#index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

d={"one":1,"two":2,"three":3}
for k in d:
	print(k,d[k])
for k in d.keys():
	print(k)
for v in  d.values():
	print(v)
dd={k:v for k,v in d.items()}
print(dd)
dd={k:v for k,v in d.items() if v % 2==0}
print(dd)




#str(字典)返回字典的字符串格式
#clear清空字典
#iteam返回字典的键值对组成的元组格式
#keys返回字典的键组成的一个结构
#values返回一个科迭代的结构
#get根据制定键返回相应的值，好处是 可以设置默认值 print(d.get("one",100))
#fromkeys使用指定的序列作为键 ，使用一个值作为字典的所有的键的值
'''
定义一个学生的类，用来形容学生
'''
#定义一个空的类
class Student():
	#一个空类，pass代表跳过
	#此处pass必须有
	pass
#定义一个对象
mingyue=Student()
#定义一个类来描述听python的学生
class PythonStudent():
	#用None给不确定的值赋值
	name = None
	age = 18
	course = "python"

	def doHomework(self):
		print("I 在做作业")
		return None
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()




