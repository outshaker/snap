Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> dir(json)
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
>>> # load
>>> # save
>>> # save => dump
>>> # [1,2,3,4]
>>> json_string = '[1,2,3,4]'
>>> json.loads(json_string)
[1, 2, 3, 4]
>>> list_ = json.loads(json_string)
>>> list_
[1, 2, 3, 4]
>>> for x in list_:
	print(x)

	
1
2
3
4
>>> sum(list_)
10
>>> example = '{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}'
>>> obj = json.loads(example)
>>> obj
{'glossary': {'title': 'example glossary', 'GlossDiv': {'title': 'S', 'GlossList': {'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'Standard Generalized Markup Language', 'Acronym': 'SGML', 'Abbrev': 'ISO 8879:1986', 'GlossDef': {'para': 'A meta-markup language, used to create markup languages such as DocBook.', 'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}}}
>>> dir(obj)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> obj['glossary']
{'title': 'example glossary', 'GlossDiv': {'title': 'S', 'GlossList': {'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'Standard Generalized Markup Language', 'Acronym': 'SGML', 'Abbrev': 'ISO 8879:1986', 'GlossDef': {'para': 'A meta-markup language, used to create markup languages such as DocBook.', 'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}}
>>> obj.glossary
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    obj.glossary
AttributeError: 'dict' object has no attribute 'glossary'
>>> obj['glossary']['title']
'example glossary'
>>> from random import randint
>>> numbers = []
>>> for i in range(50): numbers.append(str(randint(1,100)))

>>> print(numbers)
['79', '62', '64', '19', '11', '62', '28', '69', '79', '95', '96', '54', '47', '7', '22', '82', '56', '19', '89', '58', '33', '20', '55', '42', '14', '34', '63', '9', '33', '69', '54', '27', '54', '53', '89', '14', '44', '60', '53', '4', '99', '34', '13', '75', '56', '12', '84', '97', '85', '6']
>>> json.dumps(numbers)
'["79", "62", "64", "19", "11", "62", "28", "69", "79", "95", "96", "54", "47", "7", "22", "82", "56", "19", "89", "58", "33", "20", "55", "42", "14", "34", "63", "9", "33", "69", "54", "27", "54", "53", "89", "14", "44", "60", "53", "4", "99", "34", "13", "75", "56", "12", "84", "97", "85", "6"]'
>>> export_string
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    export_string
NameError: name 'export_string' is not defined
>>> export_string = json.dumps(numbers)
>>> export_string
'["79", "62", "64", "19", "11", "62", "28", "69", "79", "95", "96", "54", "47", "7", "22", "82", "56", "19", "89", "58", "33", "20", "55", "42", "14", "34", "63", "9", "33", "69", "54", "27", "54", "53", "89", "14", "44", "60", "53", "4", "99", "34", "13", "75", "56", "12", "84", "97", "85", "6"]'
>>> person = {}
>>> person['name'] = 'john'
>>> person['height'] = 198
>>> person['weight'] = 90.0
>>> person['gender'] = 'male'
>>> person['birthday'] = {'year': 1980, 'month': 1, 'day': 23}
>>> person['nation'] = 'US'
>>> person['language'] = 'en'
>>> person['hobby'] = 'swimming'
>>> person
{'name': 'john', 'height': 198, 'weight': 90.0, 'gender': 'male', 'birthday': {'year': 1980, 'month': 1, 'day': 23}, 'nation': 'US', 'language': 'en', 'hobby': 'swimming'}
>>> json.dumps(person)
'{"name": "john", "height": 198, "weight": 90.0, "gender": "male", "birthday": {"year": 1980, "month": 1, "day": 23}, "nation": "US", "language": "en", "hobby": "swimming"}'
>>> export_person = json.dumps(person)
>>> f = open("C:\\Users\\LiaoNotebook\\Desktop\\person.json","a")
>>> f.write(export_person, encode='utf8')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    f.write(export_person, encode='utf8')
TypeError: TextIOWrapper.write() takes no keyword arguments
>>> f.close()
>>> f = open("C:\\Users\\LiaoNotebook\\Desktop\\person.json","a", encoding='utf8')
>>> f.write(export_person)
171
>>> f.close()
>>> 