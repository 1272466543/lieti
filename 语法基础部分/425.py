'''汉诺塔 
1.每次移动一个盘子
2.任何时候大盘子在下 小盘子在上

1.n=1  
	A->C
2.n=2  
	A->B
	A->C
	B->C
3.n=3
	1.把A上的两个盘子，通过C移动到B上去，调用递归实现
	2.把A上剩余的一个最大的盘子移动到C上去，A->C
	3.把B上两个盘子，借助于A，挪到C上去，调用递归
4.n=n
	1.把A上的n-1个盘子借助于C移动到B上去，调用递归
	2.把A上的最大盘子，也是唯一一个，移动到C上，A->C
	3.把B上的n-1个盘子，借助于A，移动到C上，调用递归
'''
'''
n:代表几个盘子
a:代表第一个盘子
b:代表第二个盘子
c:代表第三个盘子
'''

def hano(n,a,b,c):
	if n==1:
		print(a,"-->",c)
		return None
	if n==2:
		print(a,"-->",b)
		print(a,"-->",c)
		print(b,"-->",c)
		return None
	#把n-1个盘子，从a塔借助于c塔移到b塔上去
	hano(n-1,a,c,b)
	print(a,"-->",c)
	#把n-1个盘子，从b塔借助于a塔移到c上去
	hano(n-1,b,a,c)
a="A"
b="B"
c="C"
n=3
hano(n,a,b,c)

#indx表示的是list的下标

a = [1,2,3,4,5]
b = [i*10 for i in a]
print(b)


a = [x for x in range(1,35)]
b = [m for m in a if m % 2 ==0]
print(a)
print(b)


a=[1,2,3,4,5]
b=[2,4,6,8,10]
c = [d+e for d in a for e in b]
print(c)

#append 在末尾追加一个内容
#insert(index，data)，插入位置是index的前面，指定位置插入
#del删除  
#pop(),从对位拿出一个元素，即把最后一个元素取出来
#remove：在列表中删除指定元素
#clear：清空
#reverse：翻转
#extend：扩展列表，两个列表，把最后一个直接平接到最后一个上
#count;查找列表中指定值或元素出现的次数
#copy 拷贝


