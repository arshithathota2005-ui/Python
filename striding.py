Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:7]
'gna'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'

b="work  until you succeed"
a[4:10]
'gnan'
b[4:10]
'  unti'
b[5:11]
' until'
b[[5:10]
  
SyntaxError: invalid syntax
b[5:10]
  
' unti'
b[5:9]
  
' unt'

b="work until you succeed"
  
b[4:10]
  
' until'
b[5:10]
  
'until'
b[15:22]
  
'succeed'
b[11:14]
  
'you'
b[1:4]
  
'ork'
b[0:4]
  
'work'

c="Vijayawada is a royal city"
  
c[21:26]
  
' city'
c[16:21]
  
'royal'
c[0:10]
  
'Vijayawada'
c[11:13]
  
'is'

#Negative
  

d="Happy Teachers Day"
  

d[-14:-19]
  
''
d[-13:-18]
  
''
d[-18:-13]
  
'Happy'
d[-3:-1]
  
'Da'
d[-3:]
  
'Day'
d[-12:-5]
  
'Teacher'

h="vizag is city of destiny"
  
h['
  
SyntaxError: unterminated string literal (detected at line 1)
h[-7:]
  
'destiny'
h[-24:-16]
  
'vizag is'



#striding
  
a="Machine learning"
  
a[::3]
  
'Mheeng'
a[::5]
  
'Mnag'
a[::2]
  
'Mcielann'
a[::9]
...   
'Me'
>>> a[3:11]
...   
'hine lea'
>>> a[5:]
...   
'ne learning'
>>> a[:7]
...   
'Machine'
>>> b="Cloud Computing"
...   
>>> a[1:7:2]
...   
'ahn'
>>> b[1:7:2]
...   
'lu '
>>> a[2:13:3}
...   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[2:13:3]
...   
'cnlr'
>>> b[2:13:3]
...   
'o mt'
>>> b[4:14:5]
...   
'dp'
>>> b[3:12:6]
...   
'up'
>>> 
>>> i = "pyhton course"
...   
>>> a[-1:-9:-3]
...   
'gne'
>>> i[-1:-9:-3]
...   
'eu '
>>> i[-2:-12:-4]
...   
'sct'
>>> a[-4:-13:-5]
...   
'n '
>>> i[-4:-13:-5]
...   
'uo'
>>> i[-6:-12:-2]
...   
'cnt'
>>> i[::-1]
...   
'esruoc nothyp'
>>> i[-9:-5:-2}
...   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> i[-9:-5:-]
...   
SyntaxError: invalid syntax
>>> i[-9:-5:-2]
...   
''
