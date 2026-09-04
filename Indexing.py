Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> a="Vijayawada"
>>> a[1]
'i'
>>> a[5]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Vijaya'
>>> b="i am arshi"
>>> b[5]+b[6]+b[7]+b[8]+b[9]
'arshi'
>>> a[2]+a[3]
'ja'
>>> b[2]+b[3]
'am'
>>> b[1]
' '
>>> b[4]
' '
>>> b[1]+b[4]
'  '
>>> a="I am learning python fullstack"
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]+[7]+a[8]+a[9]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[5]+a[6]+[7]+a[8]+a[9]
TypeError: can only concatenate str (not "list") to str
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[14]+a[15]+a[16]+a[18]+a[19]
'pyton'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]
'fullstack'
>>> a="time is very precious"
>>> a[-21]+a[-20]+a[-19]+a[-18]
'time'
>>> a="codegnan it solutions"
>>> a[-21]+a[-20]+a[-19]+a[-18]
'code'
>>> +a[-17]+a[-16]+a[-15]+a[-14]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    +a[-17]+a[-16]+a[-15]+a[-14]
TypeError: bad operand type for unary +: 'str'
>>> a[-17]+a[-16]+a[-15]+a[-14]
'gnan'
>>> a[-9]+a[-8]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]
'soolution'
