
import math
def quadratic(a,b,c):
	if not isinstance(a and b and c,(int,float)):
		raise TypeError('bad operand type')
	drt=b*b-4*a*c
	if drt<0:
		print("该方程无解")
		return None,None

	else:
		x=(-b+math.sqrt(b*b-4*a*c))/2*a
		y=(-b-math.sqrt(b*b-4*a*c))/2*a
		return x,y
x1,x2=quadratic (2,2,2)
print(x1,x2)


def product(*numbers):
	if numbers==0: 
		raise TypeError 
	sum = 1
	for n in numbers:
		sum=sum*n
	return sum
x=product(1,2,3,4,5)
print(x)



def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
x=fact(6)
print(x)  #递归函数

