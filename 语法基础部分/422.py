
x=input("请输入性别")
print("请输入你的性别是:{0}".format(x))
if x=="nan":
	print("1")
else:
	print("0")

print("0123")



#continue 无条件结束本次循环进入下一次循环


def hello(p):
	print("{0},你还能".format(p))
	print("sorrry")
s="123"
hello(s)

for row in range(1,10):
	for sol in range(1,row+1):
		print(row*sol,end=" ")
	print("")

def printline(row):
	for col in range(1,row+1):
		print(row*col,end=" ")
	print("")
for row in range(1,10):
	printline(row)





################

def RabbitNum(mouth):
	for x in range(0,mouth):
		if len(rabbit) < 3:
			rabbit.append(1)
		else:
			rabbit.append(rabbit[-1]+rabbit[-3])
	return rabbit[-1]
rabbit = []
mouth = 10
print("一共有{0}只兔子".format(RabbitNum(mouth)))



def rabbits(mouth):
	if mouth<=3:
		return 1
	return rabbits(mouth-1)+rabbits(mouth-3)
print("一共有{0}只兔子".format(rabbits(mouth)))