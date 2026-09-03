Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
int(3)
3
int(3.5)
3
int("hi")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(3+5j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(3+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(3)
3.0
float(3.5)
3.5
float("arshi")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float("arshi")
ValueError: could not convert string to float: 'arshi'
float(5+3j)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float(5+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> str(13)
'13'
>>> str(3.55)
'3.55'
>>> str("code")
'code'
>>> str(3=6j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> str(3+6j)
'(3+6j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(3)
(3+0j)
>>> complex(3.5)
(3.5+0j)
>>> comple("Hi")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    comple("Hi")
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex("HI)
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> complex("True")
...         
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex("True")
ValueError: complex() arg is a malformed string
>>> complex("False")
...         
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex("False")
ValueError: complex() arg is a malformed string
>>> bool(2)
...         
True
>>> bool(3.5)
...         
True
>>> bool("Arshi")
...         
True
>>> bool(3+5j)
...         
True
>>> bool(True)
...         
True
>>> bool(False)
...         
False
>>> 
>>> 
>>> 
