Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DICTIONARY 1
d={'name':'Anita','age':22,'city':'Delhi','course':'Python','marks':[85,90,78],'active':True,'skills':('SQL','Excel'),'id':101,'email':'anita@example.com'}
d
{'name': 'Anita', 'age': 22, 'city': 'Delhi', 'course': 'Python', 'marks': [85, 90, 78], 'active': True, 'skills': ('SQL', 'Excel'), 'id': 101, 'email': 'anita@example.com'}
d['name']
'Anita'
d['age']
22
d['city']
'Delhi'
d['course']
'Python'
d['marks']
[85, 90, 78]
d['marks'][0]
85
d['marks'][2]
78
d['marks'][1]
90
d['active']
True
d['skills']
('SQL', 'Excel')
d['skills'][0]
'SQL'
d['skills'][1]
'Excel'
d['id']
101
d['email']
'anita@example.com'
d(keys[:])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d(keys[:])
NameError: name 'keys' is not defined
d(:)
SyntaxError: invalid syntax
keys = list(d.keys())   


d
{'name': 'Anita', 'age': 22, 'city': 'Delhi', 'course': 'Python', 'marks': [85, 90, 78], 'active': True, 'skills': ('SQL', 'Excel'), 'id': 101, 'email': 'anita@example.com'}
d[key]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[key]
NameError: name 'key' is not defined. Did you mean: 'keys'?
list(d)
['name', 'age', 'city', 'course', 'marks', 'active', 'skills', 'id', 'email']
d.values()
dict_values(['Anita', 22, 'Delhi', 'Python', [85, 90, 78], True, ('SQL', 'Excel'), 101, 'anita@example.com'])


#DICTIONARY 2
d=['a',100,2.5,False,[10,20],'hi',None,(1,2),'bye']
d
['a', 100, 2.5, False, [10, 20], 'hi', None, (1, 2), 'bye']
d[:3]
['a', 100, 2.5]
d[-4:]
['hi', None, (1, 2), 'bye']
d[2:6]
[2.5, False, [10, 20], 'hi']
d[3:]
[False, [10, 20], 'hi', None, (1, 2), 'bye']
d[:5]
['a', 100, 2.5, False, [10, 20]]
d[1:]
[100, 2.5, False, [10, 20], 'hi', None, (1, 2), 'bye']
d[-1:]
['bye']
d[:-1]
['a', 100, 2.5, False, [10, 20], 'hi', None, (1, 2)]
d[::-1]
['bye', (1, 2), None, 'hi', [10, 20], False, 2.5, 100, 'a']
d[::2]
['a', 2.5, [10, 20], None, 'bye']
d[1::2]
[100, False, 'hi', (1, 2)]
d[::3]
['a', False, None]
d[::-2]
['bye', None, [10, 20], 2.5, 'a']
d[-7:-3]
[2.5, False, [10, 20], 'hi']
d[2:6]
[2.5, False, [10, 20], 'hi']
d[::1]
['a', 100, 2.5, False, [10, 20], 'hi', None, (1, 2), 'bye']




#DICTIONARY 3
d=[None,'data',42,3.5,[7,8,9],{'a':1},'ok',0,(5,6,7)]
d
[None, 'data', 42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0, (5, 6, 7)]
d[5:]
[{'a': 1}, 'ok', 0, (5, 6, 7)]
d[:6]
[None, 'data', 42, 3.5, [7, 8, 9], {'a': 1}]
d[:5]
[None, 'data', 42, 3.5, [7, 8, 9]]
d[-3:]
['ok', 0, (5, 6, 7)]
d[1:6]
['data', 42, 3.5, [7, 8, 9], {'a': 1}]
d[2:]
[42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0, (5, 6, 7)]
d[:43]
[None, 'data', 42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0, (5, 6, 7)]
d[:3]
[None, 'data', 42]
d[1:]
['data', 42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0, (5, 6, 7)]
d[:-1]
[None, 'data', 42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0]
d[::-1]
[(5, 6, 7), 0, 'ok', {'a': 1}, [7, 8, 9], 3.5, 42, 'data', None]
d[::2]
[None, 42, [7, 8, 9], 'ok', (5, 6, 7)]
d[1::2]
['data', 3.5, {'a': 1}, 0]
d[::3]
[None, 3.5, 'ok']
d[::-2]
[(5, 6, 7), 'ok', [7, 8, 9], 42, None]
>>> d[-7:-2]
[42, 3.5, [7, 8, 9], {'a': 1}, 'ok']
>>> d[2:6]
[42, 3.5, [7, 8, 9], {'a': 1}]
>>> d[2:5]
[42, 3.5, [7, 8, 9]]
>>> d[::1]
[None, 'data', 42, 3.5, [7, 8, 9], {'a': 1}, 'ok', 0, (5, 6, 7)]
>>> 
>>> 
>>> #DICTIONARY 4
>>> 
>>> d=[1,'two',3.0,[4,5],('six',6),True,{'key':'value'},None,'last']
>>> d
[1, 'two', 3.0, [4, 5], ('six', 6), True, {'key': 'value'}, None, 'last']
>>> d[:5]
[1, 'two', 3.0, [4, 5], ('six', 6)]
>>> d[:4]
[1, 'two', 3.0, [4, 5]]
>>> d[-4:]
[True, {'key': 'value'}, None, 'last']
>>> d[1:5]
['two', 3.0, [4, 5], ('six', 6)]
>>> d[1:8]
['two', 3.0, [4, 5], ('six', 6), True, {'key': 'value'}, None]
>>> d[::-1]
['last', None, {'key': 'value'}, True, ('six', 6), [4, 5], 3.0, 'two', 1]
