'''
#模块的搜索路径和储存
import sys
print(type(sys.path))
print(sys.path)
for p in sys.path:
	print(p)
'''
#添加搜索路径
'''
sys.path.append(dir)


'''
'''
#包的导入操作
import package_name
#可以使用__init__.py中的内容
#使用方式
package_name.func_name
package_name.class_name.func_name()
'''

'''
import package.module #导入包中某一个具体的模块
	package.module.func_name
	package.module.class.fun()
	package.module.class.var
'''


