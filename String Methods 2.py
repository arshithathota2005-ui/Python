Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#replace
a="wait until you succed"
a.replace("wait","work")
'work until you succed'
b="i am arshitha"
b.replace("i am","my name")
'my name arshitha'
c.replace("a","r")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c.replace("a","r")
NameError: name 'c' is not defined
b.replace("a","r")

'i rm rrshithr'


#upper()
a="arshitha"
a.upper()
'ARSHITHA'
b="THOTA"
#lower
b.lower()
'thota'
a.upper(0)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.upper(0)
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'A'
#capitalize
a.capitalize()
'Arshitha'
#title
b="My name is arshitha"
b.title()
'My Name Is Arshitha'


#startswith()
a="i am Arshitha"
a.startswith("i")
True
#endswith()
a.endswith("a")
True
#isalpha
a.isalpha()
False
a="Arshtiha"
a.isalpha()
True
b=123
b.isnum()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.isnum()
AttributeError: 'int' object has no attribute 'isnum'
b="123
SyntaxError: unterminated string literal (detected at line 1)
b="1234"
b.isnum()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
#isdigit()
b.isdigit()
True
a.isalnum()
True
b.isalnum()
True
c="123Arshi"
c.isalnum()
True


#strip()
#lstrip(),rstrip()
a="    Arshitha     "
a.strip()
'Arshitha'
a.lstrip()
'Arshitha     '
a.rstrip()
'    Arshitha'


#Concatination
a="thota"
b="arshitha"
print(a+b)
thotaarshitha
print(a+" "+b)
thota arshitha
print((a+" "+b).title())
Thota Arshitha


split()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    split()
NameError: name 'split' is not defined
#split()
a="my name is Arshitha"
a.split()
['my', 'name', 'is', 'Arshitha']
b="hello ram"
b.split()
['hello', 'ram']


#join()
a="arshitha","Thota"
"".join(a)
'arshithaThota'
" ".join(a)
'arshitha Thota'
"9".join(a)
'arshitha9Thota'
b="Arshitha"
"i".join(b)
'Airisihiiitihia'

#formatting
a=5
b=6
print(a+b)
11
print("the sum is",a+b)
the sum is 11
city="IBM"
print("city is",city)
city is IBM

  
#format
a="motu"
b="pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello{}".format(a,b))
hello motu hellopathlu
/hello motu hellopathlu
SyntaxError: invalid syntax

#fstring()
a="Thota"
b="Arshi"
print(f"hello {a}{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a}{b}")
      
hello ThotaArshi
print(f"hello {a} {b}")
      
hello Thota Arshi
print(f"hello {a} hello{b}")
      
hello Thota helloArshi
print(f"hello {a} hello {b}")
      
hello Thota hello Arshi

fname="Thota"
...       
>>> lname="Arshitha"
...       
>>> print("{} {}".format(a,b))
...       
Thota Arshi
>>> print("{} {}".format(fname,lanme))
...       
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print("{} {}".format(fname,lanme))
NameError: name 'lanme' is not defined. Did you mean: 'lname'?
>>> print("{} {}".format(fname,lname))
...       
Thota Arshitha
>>> print(f"{fname} {lname})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"{fname} {lname}")
...       
Thota Arshitha
>>> 
>>> 
>>> fname="Thota"
...       
>>> lname="Arshitha"
...       
>>> print("{} {}".format(fname,lname))
...       
Thota Arshitha
>>> print("{} {}".format(fname,lname))
...       
Thota Arshitha
>>> print(f"{fname} {lname}")
...       
Thota Arshitha
>>> print(f"hello{fname} {lname}")
...       
helloThota Arshitha
>>> print(f"hello {fname} {lname}")
...       
hello Thota Arshitha
>>> 
>>> a=3
...       
>>> b=5
...       
>>> print("the sum is {} {}".format(a,b))
...       
the sum is 3 5
>>> c=a+b
...       
>>> print("the sum is {}".format(c))
...       
the sum is 8
>>> print(f"the sum is{a+b}")
...       
the sum is8
>>> print("the sum is {a+b}".format(a,b))
...       
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print("the sum is {a+b}".format(a,b))
KeyError: 'a+b'
>>> print("the sum is {}".format(a+b))
...       
the sum is 8
