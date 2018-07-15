#第一题
print('请输入两个整型数，用逗号隔开：')
num1,num2 = eval(input())
if num1 > num2:
	print(num1,'是两个数中最大的数')
else:
	print(num2,'是两个数中最大的数')
#第二题
print('请分别输入两个字符串')
str1,str2 = input().split()
i = 0
if len(str1) > len(str2):
	y = str2
	j = str1
else:
	y = str1
	j = str2
q = len(y)
if str1 ==str2:
	print(str1,'=',str2)
elif str1[q-1] == str2[q-1]:
	print(y,'<',j)
else:
	while i < len(y):
		if ord(str1[i]) > ord(str2[i]):
			print(str1,'>',str2)
			break
		elif ord(str1[i]) < ord(str2[i]):
			print(str1,'<',str2)
			break
		else:
			i +=  1
#第三题
y = input('输入一个字符串：')
i = 0
q = 0
w = 0
e = 0
while i < len(y):
	s = y[i]
	if s.islower():
		q += 1
	elif s.isdigit():
		w += 1
	elif s.isupper():
		e += 1
	i += 1
print('小写字母个数：',q)
print('大写字母个数：',e)
print('数字的个数',w)
#第四题
s = input('请输入一串字符：')
print(s.split())
print(s.title())
