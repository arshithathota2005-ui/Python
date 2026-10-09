'''def greetings(name):
    print("Welcome",name)'''

'''a=10
b=20
print("sum is",a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a*b)'''

#details = {"idnos":[10,20,30],"name":["Arshi","Asmi","Remo"],"marks":[90,80,60]}


'''if  __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    print(a)'''


'''def dummy():
    if __name__=="__main__":
        print("this program is running as script")
    else:
        print("this program is running as mudule")
dummy()'''

#math module

'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(4))
print(math.pow(2,4))
print(math.log(10))
qprint(math.cos(60))
print(math.tan(45))
print(math.ceil(3.9))
print(math.ceil(6.9))
print(math.floor(6.9))'''

'''from math import pi,log,sqrt,log,tan
print(pi,log(20),sqrt(30),log(40),tan(80))'''


#sys module
import sys
'''print(sys.path)

for i in sys.path:
    print(i)'''
#print(sys.version)

#os module
import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("//Users//apple//Desktop"))
#print(os.listdir())



#random module
#sample
'''import random
a=random.sample(range(10,50),5)
print(a)'''

#randint
'''import random
a=random.randint(3,13)
print(a)'''

#choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''


#roll Dice
'''import random
while True:
    a = int(input("Roll of Dice"))
    b=random.randint(1,6)
    print(b)
    op = int(input(options: 1.Yes
                   2.No: ))
    if op==1:
        continue
    else:
        break'''


#calender module
'''import calendar
year =2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year = 2027
print(calendar.calendar(year))'''

'''while True:
    
    import calendar
    a=int(input("enter year"))
    b=int(input("enter month"))
    print(calendar.month(a,b))'''

        
#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''


'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"week day and year day is {b.tm_wday}and {b.tm_yday}")
'''











'''import random
import time
for i in range(10):
    c=random.randint(3,33)
    time.sleep(2)
    print(c)'''


#regular expressions (regax)

'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w-> it matches alphanumeric
\W-> it matches non-alphanumeric
\d-> it matches any digit
\D-> it matches non-digits
\s-> it represents white spaces
\S-> it represents non-white spaces'''

import re
a="code map money cash cap maths cup cat mug mat"
'''b=re.compile(r"m\w\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)
'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''b=re.findall(r"m\w+",a)
print(b)'''

'''c=re.findall(r"c\w+",a)
print(c)'''


#split()
'''c=re.split(r"m",a)
print(c)

d=re.split(r"\s",a)
print(d)'''

#sub()
'''e = re.sub(r"m","w",a)
print(e)'''


'''b = "arshi1asmi23thota4"
d=re.split(r"\d+",b)
c=re.findall(r"\d+",b)
print(c)
print(d)'''

'''b="year 2026 month 10 date 6"
c=re.findall(r"\d+",b)
d=re.findall(r"\D+",b)
e=re.findall(r"\d",b)
f=re.findall(r"\D",b)
print(c)
print(d)
print(e)
print(f)

'''































