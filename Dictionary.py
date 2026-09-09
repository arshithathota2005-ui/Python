Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"Arshi","city":"IBM"}
print(a)
{'name': 'Arshi', 'city': 'IBM'}
typr(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    typr(a)
NameError: name 'typr' is not defined. Did you mean: 'type'?
b={"name","arshi"}
type(b)
<class 'set'>


#keys
a.keys()
dict_keys(['name', 'city'])
a={"year":2026,"month":"sep","date":9}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'sep', 9])
a.value()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])
a["year"]
2026
a[2026]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[2026]
KeyError: 2026
a.get("year")
2026

#update()
a={"name":"Arshi","city":"IBM"}
a.update({"year":2026})
a
{'name': 'Arshi', 'city': 'IBM', 'year': 2026}
a.update({"mail":"fsrd@gmail.com"},{"phone":7328329817})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.update({"mail":"fsrd@gmail.com"},{"phone":7328329817})
TypeError: update expected at most 1 argument, got 2
a.update({"mail":"fsrd@gmail.com","phone":7328329817})
a
{'name': 'Arshi', 'city': 'IBM', 'year': 2026, 'mail': 'fsrd@gmail.com', 'phone': 7328329817}

#setdefault
a={"hour":3,"min":12}
a.setdefault("sec":13)
SyntaxError: invalid syntax
a.setdefault("sec",13)
13
a
{'hour': 3, 'min': 12, 'sec': 13}

#pop
b={"week":"wed","date":9}
b.pop()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 argument, got 0
>>> b.pop("date")
9
>>> b
{'week': 'wed'}
>>> 
>>> 
>>> #popitem
>>> a={"country":"india","state":"AP"}
>>> a.popitem()
('state', 'AP')
>>> a
{'country': 'india'}
>>> a.update({"city":"IBM"})
>>> a
{'country': 'india', 'city': 'IBM'}
>>> a.popitem("city")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.popitem("city")
TypeError: dict.popitem() takes no arguments (1 given)
>>> 
>>> #copy
>>> a={"name":"Arshi","city":"IBM","mail":"ars@gmail.com"}
>>> a.copy()
{'name': 'Arshi', 'city': 'IBM', 'mail': 'ars@gmail.com'}
>>> len(a)
3
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("city")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> 
>>> a={"name":"arshi","year":2026,"name":"arshi"}
>>> print(a)
{'name': 'arshi', 'year': 2026}
>>> a={"name":"arshi","year":2026,"name":"asmi"}
>>> a
{'name': 'asmi', 'year': 2026}
>>> a={"name":"arshi","year":2026,"name1":"arshi"}
>>> a
{'name': 'arshi', 'year': 2026, 'name1': 'arshi'}
>>> 
>>> a={"id":[10,13,15],"name":["arshi","manu","sweety"],"city":["vjy","gtr","rrmp"]}
>>> a
{'id': [10, 13, 15], 'name': ['arshi', 'manu', 'sweety'], 'city': ['vjy', 'gtr', 'rrmp']}
>>> a.keys()
dict_keys(['id', 'name', 'city'])
>>> a.values()
dict_values([[10, 13, 15], ['arshi', 'manu', 'sweety'], ['vjy', 'gtr', 'rrmp']])
>>> a.items()
dict_items([('id', [10, 13, 15]), ('name', ['arshi', 'manu', 'sweety']), ('city', ['vjy', 'gtr', 'rrmp'])])
>>> {'name': 'Arshi', 'city': 'IBM', 'mail': 'ars@gmail.com'}
{'name': 'Arshi', 'city': 'IBM', 'mail': 'ars@gmail.com'}
>>> 
>>> 
>>> 
