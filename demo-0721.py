# 0721 上課紀錄，請注意這個程式不能直接執行唷

# Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.


# 有回傳值的函數
>>> def foo(): return "bar"

>>> foo()
'bar'

# 沒回傳值的函數
>>> def baz():
	print("bar")

>>> baz()
bar
>>> x = foo()
>>> x
'bar'
>>> y = baz()
bar
>>> y

# scratch 上面改 x 內容的寫法，但 python 上面會失敗
>>> def foo2(value):
	x = value
	
>>> x
'bar'
>>> foo2('barbar')
>>> x
'bar'

# 改成這樣子就可以在 python 上面跑了
>>> def foo3(value):
	global x
	x = value

	
>>> x
'bar'
>>> foo3('barbar')
>>> x
'barbar'

# 介紹比較特殊的函數寫法: 遞迴函數
>>> def loop():
	print('loop')
	loop()

# 示範不斷呼叫自己的函數
>>> loop()
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loop
loopTraceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    loop()
  File "<pyshell#28>", line 3, in loop
    loop()
  File "<pyshell#28>", line 3, in loop
    loop()
  File "<pyshell#28>", line 3, in loop
    loop()
  [Previous line repeated 201 more times]
  File "<pyshell#28>", line 2, in loop
    print('loop')
KeyboardInterrupt
>>> # 遞回函式

# 用遞回函數的方式去計算數字加總
>>> def my_sum(n, s=0):
	print(n,s)
	if n > 0:
		my_sum(n-1, s+n)
	else:
		return s

	
>>> my_sum(10)
10 0
9 10
8 19
7 27
6 34
5 40
4 45
3 49
2 52
1 54
0 55
>>> s = my_sum(10)
10 0
9 10
8 19
7 27
6 34
5 40
4 45
3 49
2 52
1 54
0 55
>>> s
>>> s

# 前面抓不到回傳值，修改成這個版本之後成功抓到數字加總的回傳值
>>> def my_sum(n, s=0):
	print(n,s)
	if n > 0:
		return my_sum(n-1, s+n)
	else:
		return s

	
>>> s = my_sum(10)
10 0
9 10
8 19
7 27
6 34
5 40
4 45
3 49
2 52
1 54
0 55
>>> s
55

# 示範用 for 做數字加總的方法
>>> list1 = [1,2,3]
>>> s = 0
>>> for i in range(len(list1)):
	s += list1[i]

>>> # s = s + list[i]
>>> for i in range(len(list1)): print(i)

0
1
2

# 介紹 range() 的用法
>>> for i in range(10): print(i)

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
>>> list[0]
list[0]
>>> list1[0]
1
>>> list1[1]
2
>>> list1[2]
3
>>> list2 = ['a', 'b', 'c']
>>> list2[0]
'a'
>>> list2[1]
'b'
>>> list2[2]
'c'

# 介紹 range() 會跳出錯誤的情況
>>> for i in range(10): print(list2[i])

a
b
c
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for i in range(10): print(list2[i])
IndexError: list index out of range
>>> len(list2)
3

# for x in some_list 比較新的寫法，語法看起來更簡潔
>>> for x in list2: print(x)

a
b
c

# 介紹 dir() 的用法，可以查詢一些 python 物件的功能
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list2.pop()
'c'
>>> list2
['a', 'b']

# 統計 list2 中， 'a' 出現的次數
>>> list2.count('a')
1
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# python 內的說明功能
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  exit(name, eof)
 |  
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

# 輸入 quit 可以離開
help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.


>>> for i in range(len(list1)):
	s += list1[i]


>>> s
12

# 記得數字加總之前要把 s 清空
>>> s=0
>>> for i in range(len(list1)):
	s += list1[i]

	
>>> s
6

# 把上面的程式包成一個函數
>>> def my_sum2(list_):
	s = 0
	for i in range(len(list_)):
		s += list_[i]
	return s

>>> my_sum2(list1)
6

# 直接寫一個 list 進去也可以，不一定要用變數
>>> my_sum2([1,1,1,1,1,11,1,1,1,11,1,1,11])
43

# 簡單帶過 tuple, 一開始比較少用到這個
>>> (1,2,3)
(1, 2, 3)
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# 介紹 dict 字典
>>> d = {}
>>> d['key'] = '123'
>>> d
{'key': '123'}
>>> list1
[1, 2, 3]
>>> ['123','456','789']
['123', '456', '789']

# 比較 dict 和 list 的差異
>>> d2 = {0: 'a', 1: 'b', 2: 'c'}
>>> d2
{0: 'a', 1: 'b', 2: 'c'}
>>> d2[0]
'a'
>>> d2[1]
'b'
>>> d2[2]
'c'

# dict 會出現的錯誤
>>> d2['xxx']
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    d2['xxx']
KeyError: 'xxx'

# list 會出現的錯誤
>>> list1[9999]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    list1[9999]
IndexError: list index out of range
>>> 9999 > len(list1)
True

# 示範怎麼寫程式不會出錯
>>> i = 9999
>>> if i > len(list1):
	print("超過範圍")
else:
	print(list1[i])

	
超過範圍

>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> list2
['a', 'b']

# 問問題，怎麼讓 list 可以顛倒排序？
>>> list2 = ['z', 'x', 'c', 'b', 'n']

# 排序之前記得存一份原本的資料
>>> list3 = list2.copy()
>>> list3
['z', 'x', 'c', 'b', 'n']
>>> list3.sort(reverse=True)
>>> list3
['z', 'x', 'n', 'c', 'b']
>>> 