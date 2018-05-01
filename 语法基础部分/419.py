
print('hello werld')
print('''hello world...hello...\\world\\''',41235)
#ord('A')=65
#chr(25991)='文'
#len('ABC')=3 len 多少个字符
print('Hi, %s, you have $%s.' % ('Michael', 1000000))
print("HI,{0},you have${1}".format('MIxin',10000))
s1=72
s2=85
r=s1/s2*100
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', r))
#.append('***')追加指定元素
#.insert(1, '***')插入指定元素到指定位置
#.pop(？)删除指定元素.pop()删除最后一个元素
#****[？] = '***'替换指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])


'''s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
h=1.75
w=80.5
bmi=w/(h*h)
if bmi<18.5:
	print('过轻')
elif 18.5<=bmi<25:
	print('正常')
elif 25<=bmi<28:
	print('过重')
elif 28<=bmi<32:
	print('肥胖')
else :
	print('严重肥胖')
#range(5)生成的序列是从0开始小于5的整数 
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#删除一个key，用pop(key)方法，对应的value也会从dict中删除：
#通过in判断key是否存在：print('****' in ***）
#如果key不存在，可以返回None，或者自己指定的value：
'''>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1'''
#&与   ，  | 或
#.replace('a', 'A')a替换为A
#d代表dictionary 




#abs()绝对值
#而max函数max()可以接收任意多个参数，并返回最大的那个：
#int 整数
#hex()变为16进制

def my_abs(x):#定义一个my_abs函数
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-20))

#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。


