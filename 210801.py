Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
>>> dict1 = {'intro': 'hi', 'title': 'taiwin'}
>>> print(dict1)
{'intro': 'hi', 'title': 'taiwin'}

>>> for k,v in dict1.items():
	print(k, v.title())
	
intro Hi
title Taiwin
>>> d2 = {'dict': dict1}
>>> d2
{'dict': {'intro': 'hi', 'title': 'taiwin'}}
>>> for k,v in d2.items():
	if type(v) is dict:
		for k2,v2 in v.items():
			print(k2, v2.title())
	else:
		print(v)

		
intro Hi
title Taiwin
>>> # 字典中的字典

# 示範消除換行
>>> for i in range(10):
	print(i)
	
0
1
2
3
4
5
6
7
8
9

>>> for i in range(10):
	print(i, end='')
	
0123456789

# 示範逗號
>>> for i in range(10):
	print(i, end=', ')
	
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 

# 取消最後一個逗號
>>> for i in range(10):
	if i != 9:
		print(i, end=', ')
	else:
		print(i, end='')

		
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 包成函數
>>> def foo(_list):
	for i in range(len(_list)):
		if i != len(_list) -1:
			print(i, end=', ')
		else:
			print(i, end='')

>>> mylist = list(range(10))
>>> mylist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> foo(mylist)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
>>> def foo(_list):
	print('[', end='')
	for i in range(len(_list)):
		if i != len(_list) -1:
			print(i, end=', ')
		else:
			print(i, end='')
	print(']')

	
>>> # 加上前後方框號
>>> foo(mylist)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list2=['A','B','C']
>>> foo(list2)
[0, 1, 2]
>>> def foo(_list):
	print('[', end='')
	for i in range(len(_list)):
		if i != len(_list) -1:
			print(_list[i], end=', ')
		else:
			print(_list[i], end='')
	print(']')
	
>>> foo(list2)
[A, B, C]
>>> list2
['A', 'B', 'C']
>>> dict1.items()
dict_items([('intro', 'hi'), ('title', 'taiwin')])
>>> list(dict1.items())
[('intro', 'hi'), ('title', 'taiwin')]

# 介紹 mutable 概念
>>> a = 10
>>> def f():
	print(a)

	
>>> f()
10
>>> def g():
	a = 20
	print(a)

	
>>> g()
20
>>> print(a)
10
>>> x = 10
>>> y = 20
>>> def swap(x,y):
	# x, y = y, x
	temp = x
	x = y
	y = temp
	print(x,y)

	
>>> swap(x,y)
20 10
>>> print(x,y)
10 20


>>> obj = {'x': 10, 'y':20}
>>> def h():
	obj['x'] = 30
	print(obj['x'])

	
>>> h()
30
>>> print(obj['x'])
30
>>> 
