Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
a=13
b=15
print(a+b)
28
print(a-b)
-2
print(a*b)
195
print(a//b)
0
print(a/b)
0.8666666666666667
print(a**b)
51185893014090757
print(a%b)
13

#assignments
a=12
b=14
a+=b
a
26
a-=2
a
24
a*=5
a
120
a//=4
a
30
a/=2
a
15.0
a**=2
a
225.0
a%=5
a
0.0
a
0.0
b
14
b+=3
b
17
b-=2
b
15
b*=3
b
45
b//=5
]
b
9
b/=3
b
3.0
b**=2
b
9.0
b%=3
b
0.0
a
0.0
b
0.0


#Comparision
a=3
b=5
a<b
True
a>b
False
b>a
True
b<a
False
a<=b
True
a>=b
False
a!=b
True
a=5
a==b
True
a=3
a==b
False

#Logical

a=5
b=10
a<b and b>a
True
a<b and b<a
False
a<=b and b>=a
True
>>> a>=b and b<=a
False
>>> a!=b and b!=a
True
>>> a!=b and b==a
False
>>> a<b or b>b
True
>>> a>b or b>a
True
>>> a!=b and b==a
False
>>> a<=b and b>=a
True
>>> a>=b or b<=a
False
>>> not True
False
>>> not False
True
>>> 
>>> #Identify
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> type(a) is float
False
>>> type(a) is complex
False
>>> type(a) is not float
True
>>> b=5
>>> b=5.3
>>> type(b) is float
True
>>> type(b) is not float
False
>>> ?>/./>>??
SyntaxError: invalid syntax
>>> "?:
SyntaxError: unterminated string literal (detected at line 1)
>>> 
"
>>> :?
>>> "
>>> #membership
>>> a=1,2,3,4,5,6,7
>>> 3 in a
True
>>> 9 in a
False
>>> 9 not in a
True
>>> 4 in a
True
>>> 
>>> 
>>> #bitwise
>>> a=3
>>> b=9
>>> a&b
1
>>> bin(a)
'0b11'
>>> a=3
b=4
a&b
0
bin(b)
'0b100'

a=9
b=7
a|b
15
a=4
~a
-5
b=-9
~b
8
a=5
b=3
a^b
6

a=9
b=7
a^b
14
a=7
a<<2
28
a=2
a<<2
8
b=17
b>>2
4
b>>3
2
b=5
b>>3
0
