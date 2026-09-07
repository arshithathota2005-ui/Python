Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #String Methods
>>> #len()
>>> a="Python"
>>> len(a)
6
>>> a="Python Course"
>>> len(a)
13
>>> a=""
>>> len(a)
0
>>> a=" "
>>> len(a)
1
>>> 
>>> #Count()
>>> a="twinkle twinkle little start"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
6
>>> a.count("l")
4
>>> a.count("z")
0
>>> a.count(" ")
3
>>> 
>>> #find a string
>>> a="python"
>>> a[1]
'y'
>>> a.find[y]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.find[y]
NameError: name 'y' is not defined
>>> a.find("y")
1
>>> a.find("a")
-1
>>> a.find("p")
0
>>> a.find("t")
2
>>> a.find("n")
5
>>> a.find("py")
0
>>> 
>>> 
>>> #escape sequences
>>> #\n -> new line
>>> #\t -> tab space
>>> a="idno:\name\tmoble:\nemail\ncourse\tcollege"
>>> print(a)
idno:
ame	moble:
email
course	college
>>> a="idno:2200030153\nname:Thota Arshitha\tmoble:7674989874\nemail:arshitha@gmail.com\ncourse:cse\tcollege:klu"
a
'idno:2200030153\nname:Thota Arshitha\tmoble:7674989874\nemail:arshitha@gmail.com\ncourse:cse\tcollege:klu'
print(a)
idno:2200030153
name:Thota Arshitha	moble:7674989874
email:arshitha@gmail.com
course:cse	college:klu
