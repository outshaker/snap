Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 介紹 range()
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = ['z', 'x','c']
>>> len(x)
3

# 組合程式語法去產生 for loop 可以用的資料
>>> r = range(len(x))
>>> r
range(0, 3)
>>> list(r)
[0, 1, 2]
>>> d = {'x':1,'z':2,'c':3}
>>> len(d)
3
>>> for k,v in d:
	print(k,v)

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for k,v in d:
ValueError: not enough values to unpack (expected 2, got 1)

# for k in d 可以用在 dict 上面
>>> for k in d:
	print(k)

	
x
z
c
>>> for k in d:
	print(k, d[k])

	
x 1
z 2
c 3

# 把 d.items() 轉換成 list 資料
>>> pair = list(d.items())
>>> pair
[('x', 1), ('z', 2), ('c', 3)]
>>> for i in range(len(pair)):
	print(pair[i])

	
('x', 1)
('z', 2)
('c', 3)
>>> for i in range(len(pair)):
	print(pair[i][0], pair[i][1])
	
x 1
z 2
c 3

# 用格式化字串輸出資料
>>> for i in range(len(pair)):
	print('"%s": %s, ' % (pair[i][0], pair[i][1]))

	
"x": 1, 
"z": 2, 
"c": 3, 
>>> for i in range(len(pair)):
	print('"%s": %s, ' % (pair[i][0], pair[i][1]), end='')

	
"x": 1, "z": 2, "c": 3, 
>>> for i in range(len(pair)):
	if i != len(pair) -1: # 不是最後一筆資料的時候
		print('"%s": %s, ' % (pair[i][0], pair[i][1]), end='')
	else:
		print('"%s": %s }' % (pair[i][0], pair[i][1]))

		
"x": 1, "z": 2, "c": 3 }

# 介紹日期的格式化字串 (不是 python 的東西)
>>> # 2021-08-04 15:40:12
>>> # 4/8/2021
>>> # YYYY-MM-DD HH:mm:ss
>>> # D/M/YYYY
>>> # MM 2 => 02
>>> # M 2 => 2
>>> x = 123

# 目前大家比較常用的樣板字串寫法
>>> f"x = {x}"
'x = 123'

# 介紹檔案開啟語法
>>> f = open("test.txt",'w')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f = open("test.txt",'w')
PermissionError: [Errno 13] Permission denied: 'test.txt'
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
>>> f
<_io.TextIOWrapper name='test.txt' mode='w' encoding='cp950'>
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> f.write("hihi")
4
>>> f.close()
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
f = open("test.txt",'w')
>>> f.write("\nfooooooooooooooooooooooooooooo")
31
# 在不關閉檔案的情況下更新檔案內容
>>> f.flush()
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
f = open("test.txt",'w+')
>>> f.write("\nbarrrrrrrr")
11
>>> f.flush()
>>> 
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
>>> f.write('\nbuzzzz')
7
>>> f.flush()
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
# a 檔案附加模式，寫入的檔案會在最後面出現，不會蓋掉原本的內容
f = open("test.txt",'a')
>>> f.write('\nfooo')
5
>>> f.flush()
>>> f
<_io.TextIOWrapper name='test.txt' mode='a' encoding='cp950'>
>>> f.close()
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
# 讀檔模式
f = open("test.txt",'r')
>>> f
<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp950'>
>>> f.read(10)
'\nbuzzzz\nfo'
>>> f.seek(0)
0
>>> f.readline()
'\n'
>>> f.readline()
'buzzzz\n'
>>> f.readline()
'fooo'
>>> f.seek(0)
0
>>> f.readlines()
['\n', 'buzzzz\n', 'fooo']
>>> f.seek(0)
0
>>> lines = f.readlines()
>>> lines
['\n', 'buzzzz\n', 'fooo']
>>> for line in lines:
	print(line)

	


buzzzz

fooo
>>> for line in lines:
	print(line, end="")

	

buzzzz
fooo
>>> f.write(1)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    f.write(1)
TypeError: write() argument must be str, not int
>>> x = 1
>>> str(x)
'1'
>>> f.write(str(1))
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    f.write(str(1))
io.UnsupportedOperation: not writable
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
>>> x = 10
>>> f.write("%s " % x)
3
>>> f.flush()
>>> f.close()
>>> 
======================= RESTART: C:\Users\LiaoNotebook\Desktop\open.py =======================
>>> line = f.readline()
>>> line
'10 20 '

# 字串切割函數
>>> line.split(' ')
['10', '20', '']
>>> dir(line)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 去除資料前後的空白字元
>>> line.strip()
'10 20'
>>> line.strip().split(' ')
['10', '20']
>>> arr = line.strip().split(' ')
>>> arr
['10', '20']

# 把字串資料轉換成數字
>>> list1 = []
>>> for x in arr:
	list1.append(int(x))

	
>>> list1
[10, 20]
>>> 