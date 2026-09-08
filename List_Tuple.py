Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,3.5,"python",3+4j,True,False]
type(a)
<class 'list'>
b=3.5
type(b)
<class 'float'>
c=[3.5]
type(c)
<class 'list'>

#append
a=["python","sql","c"]
a.append("c++")
a
['python', 'sql', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'sql', 'c', 'c++', ['ml', 'ai']]

#extend
a=["hi","how","are"]
a.extend("you","Doing")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.extend("you","Doing")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["you","Doing"])
a
['hi', 'how', 'are', 'you', 'Doing']


#insert
a=["blue","Green"]
a.insert(1,"white")
a
['blue', 'white', 'Green']

#index
a.index("Green")
2

#copy
a.copy()
['blue', 'white', 'Green']
b=a.copy()
b
['blue', 'white', 'Green']

 
#pop
a=["hi","Hello","How","Are","you"]
a.pop()
'you'
a
['hi', 'Hello', 'How', 'Are']
a.pop("HI")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.pop("HI")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'How'
a
['hi', 'Hello', 'Are']

#remove
a.remove("Hello")
a
['hi', 'Are']
a.remove()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)

#sort
a=["Ibm","vja","delhi","chennai"]
a.sort()
a=[1,4,23,86,35,0,22,43,12,452]
a.sort()
a
[0, 1, 4, 12, 22, 23, 35, 43, 86, 452]
b=["Ibm","vja","delhi","chennai"]
b.sort()
b
['Ibm', 'chennai', 'delhi', 'vja']
c=[1,3.5,"arshi",3+5j,True]
c.sort()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
c=[True,False]
c.sort()
c
[False, True]

#reverse
a=["mango","Apple","kiwi"]
a.reverse()
a
['kiwi', 'Apple', 'mango']
>>> b=[1,2.3,"hi",3+4j,True]
>>> b.reverse()
>>> b
[True, (3+4j), 'hi', 2.3, 1]
>>> 
>>> 
>>> #len
>>> a=["c","c++","java")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a=["c","c++","java"]
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.len()
AttributeError: 'list' object has no attribute 'len'
>>> a.length()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.length()
AttributeError: 'list' object has no attribute 'length'
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> 
>>> #count
>>> a.count("c")
1
>>> 
>>> 
>>> #clear
>>> a=["i","am","Arshi"]
>>> a.clear()
>>> a
[]
>>> a.append("Arshitha")
>>> a
['Arshitha']
>>> a.insert(0,"am")
>>> a
['am', 'Arshitha']
>>> 
>>> 
>>> #tuple()
>>> a=(3,3.5,"HI",3+5j,True,False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count(3.5j)
0
>>> a.index(True)
4
>>> 
>>> #Sets
>>> a={7,3.4,"python",True}
>>> a
{True, 3.4, 'python', 7}
>>> type(a)
<class 'set'>
>>> b={1,2,1,3,5,3,5}
>>> b
{1, 2, 3, 5}
