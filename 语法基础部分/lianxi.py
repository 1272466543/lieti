#例题01：
'''
numbers=[1,2,3,4]
number=[]
for x in numbers:
	for y in numbers:
		for z in numbers:
			if x==y or y==z or x==z:
				continue
			number.append(x*100+y*10+z)
print(len(number))


def Num(numbers):
	number=[]
	for x in numbers:
		for y in numbers:
			for z in numbers:
				if x==y or y==z or x==z:
					continue
				number.append(x*100+y*10+z)
	return number
numbers = range(1,5)
number = Num(numbers)
print(len(number))
print(number)
'''

#例题二
'''
题目：企业发放的奖金根据利润提成。利润 (I) ： 
低于或等于 10 万元时，奖金可提 10%； 
高于 10万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10
万元的部分，可提成 7.5%； 
20 万到 40 万之间时，高于 20 万元的部分，可提成 5%； 
40 万到 60 万之间时，高于 40 万元的部分，可提成 3%； 
60 万到 100 万之间时，高于 60万元的部分，可提成 1.5%， 
高于 100万元时， 
超过 100万元的部分按 1%提成， 
从键盘输入当月利润 I ，求应发放奖金总数？ 
'''
'''
def lirun(i):
	if i<=10:
		j=0.1*i
	elif 20>=i>10:
		j=0.1*10+0.75*(i-10)		
	elif 40>=i>20:
		j=0.1*10+0.75*10+0.5*(i-20)
	elif 60>=i>40:
		j=0.1*10+0.75*10+0.5*20+0.3*(i-40)
	elif 100>=i>60:
		j=0.1*10+0.75*10+0.5*20+0.3*20+0.15(i-60)
	else :
		j=0.1*10+0.75*10+0.5*20+0.3*20+0.15*40+0.1*(i-100)
	return j
i=50
#i=int(input("请输入利润："))
print("发放奖金总数为{0}".format(lirun(i)))


InMoney = int(input("请输入利润:"))
extract = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
money = [100, 60, 40, 20, 10, 0]
Bonus = 0
for i in range(0,6):
	if InMoney > money[i]:
		Bonus += (InMoney-money[i])*extract[i]
		InMoney = money[i]

print(Bonus)
'''
#例题三
'''
import math
x=0
while 1:
	if math.sqrt(x+100) % 1 == 0 and math.sqrt(x+168) % 1 == 0:
		print(x)
		break
	else:
		x += 1
'''
#例题四








