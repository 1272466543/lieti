'''
try:
	尝试某个操作，
	如果没有出现异常，任务可以完成
	如果出现异常，将异常从当前代码扔出去尝试解决
except 异常类型1:
	解决方案1:用于尝试在此处处理异常解决问题
except 异常类型2:
	解决方案2:用于尝试在此处处理异常解决问题
except (异常类型1,异常类型2...):
	解决方案:针对多个异常使用相同的处理方式
except:
	解决方案:所有异常的解决方案
else:
	如果没有出现任何异常，将会执行此处代码
finally:
	无论是否有异常都要执行的代码
#除最少一个except外，else，finally可选
'''

try:
	#num = int(input("Please input your number:"))
	num = 0
	rst = 100/num
	print("计算结果是{0}".format(rst))

#except:
#	print("输入不合理")
#	exit()

#以下语句是捕获ZeroDivisionError异常并实例化实例e

#如果是多种error的情况，需要把越具体的错误越往前放
except ZeroDivisionError as e:
	print("输入不合理")
	print(e)
	exit()
except NameError as e:
	print("名字错了")
	print(e)
	exit()
except AttributeError as e:
	print("属性有问题")
	print(e)
	exit()
#所有的异常都是继承自exception
#如果写上下面这句话 所有异常都会被拦住
#而且这句话一定是最后一个except
except Exception as e:
	print("不知道")
	print(e)
print("hhhhh")
################################################
#raise 关键字来引发异常
'''
try:
	print("abcde")
	print(123456)
	#手动引发一个异常
	raise ValueError
	print("...")

except:
'''


