Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#sets{}
a={7,3.4,"python",True}
a
{True, 3.4, 7, 'python'}
type(a)
<class 'set'>
b={1,2,1,3,5,3,5}
b
{1, 2, 3, 5}
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={4,5,6,7,8,9}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False

#issupperset()
a={5,6,7,8,9}
b={7,8,9}
a.issupperset(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.issupperset(b)
AttributeError: 'set' object has no attribute 'issupperset'. Did you mean: 'issuperset'?
a.issuperset(b)
True
b.issuperset(a)
False

 
#union()
a={1,2,3,4,5,6}
b={5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
a={1,2,3,4,6}
b={4,,5,6}
SyntaxError: invalid syntax
b={4,5,6}
a.intersection(b)
{4, 6}

#update
a={1,2,4,5,6,7}
b={6,7,8,9,10}
a.update(b)
a
{1, 2, 4, 5, 6, 7, 8, 9, 10}
b
{6, 7, 8, 9, 10}
b.update(a)
b
{1, 2, 4, 5, 6, 7, 8, 9, 10}

#difference
a={3,4,5,6,7,8}
b={1,2,3,4,5}
a.difference(b)
{8, 6, 7}
b.difference(a)
{1, 2}


#symmetric_difference()
a={1,2,3,4,5,6,7}
b={4,5,6,7,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 8, 9, 10, 11}


#difference_update
a={1,2,3,4,5,6}
b={3,4,5,7,8}
a.difference_update(b)
a
{1, 2, 6}
b.difference_update(a)
b
{3, 4, 5, 7, 8}

#intersection_update
a={1,2,3,4,5,6,7}
b={3,4,5,6,8,9}
a.intersection_update(b)
a
{3, 4, 5, 6}
b.intersection_update(a)
b
{3, 4, 5, 6}

#symmetric_difference_update
a={1,2,3,4,6,7}
b={3,4,5,6,7,8,9,10}
a.symmetric_difference_update(b)
a
{1, 2, 5, 8, 9, 10}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 6, 7}

#pop
>>> a={1,2,3,4,5,6}
>>> a.pop()
1
>>> a
{2, 3, 4, 5, 6}
>>> a.pop()
2
>>> a
{3, 4, 5, 6}
>>> a.remove(4)
>>> a
{3, 5, 6}
>>> a.pop(3)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
>>> 
>>> #discard
>>> a={1,2,3,4,5,6}
>>> a.discard(8)
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.discard(3)
>>> a
{1, 2, 4, 5, 6}
>>> 
>>> #copy
>>> a={1,2,3,5}
>>> a.copy()
{1, 2, 3, 5}
>>> 
>>> 
>>> #clear
>>> a={1,2,34}
>>> a.clear()
>>> a
set()
>>> a.add(1)
>>> a
{1}
>>> 
>>> #len
>>> a={3,4,5,6,7}
>>> len(a)
5
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(3)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.count(3)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> 
>>> #isdisjoint()
>>> a={3,2,1,4}
>>> b={6,7,8}
>>> a.isdisjoint(b)
True
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.isdisjoint(b)
False
