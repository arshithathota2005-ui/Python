#functions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''


'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)

calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("Interger Division",a//b)
    print("pow ",a**b)
    print("modular",a%b)
calculate(10,2)
calculate(2,5)
calculate(5,6)'''



'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''while True:
    def add():
        a = int(input("a value"))
        b = int(input("b value"))
        print(a+b)
    add()'''



'''def add():
    a = int(input("a value"))
    b = int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname = input("fname")
    lname = input("lanme")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(10,20)'''


'''def mul(a,b):
    return a*b
mul(10,20)'''


#print v/s return

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,4))'''



'''def cal():
    a = int(input("a value"))
    b = int(input("b value"))

    c = int(input(Options: 1.add
                  2.sub
                  3.mul))

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    if c==1:
        print(add(a,b))
    elif c==2:
        print(sub(a,b))
    elif c==3:
        print(mul(a,b))

    cal()
cal()'''


'''def cal():
    a = int(input("a value"))
    b = int(input("b value"))

    c = int(input(Options: 1.add
                  2.sub
                  3.mul))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)

    cal()
cal()'''


'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a = int(input("a value"))
    b = int(input("b value"))

    c = int(input(Options: 1.add
                  2.sub
                  3.mul))
    
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()'''
        



#split Task

'''def split():
    np  = int(input("Enter no of persons"))
    amt = int(input("Enter the amount"))   
    return amt//np
print("amount split to each person is:",split())'''


'''def split():
    n = int(input("Enter the no of persons"))
    amt = int(input("Enter the total amount"))

    sp = amt//n

    print(f"split amount is:{sp}")

split()'''


'''def split():
    n = int(input("Enter the no of persons"))
    amt = int(input("Enter the total amount"))

    print("split amount is:{}".format(amt//n))

split()'''



#keyword and positional arguments

'''def details(id,name,mailid):
    id = 10
    name = "arshi"
    mailid = "arshi@gmail.com"
    print(id,name,mailid)
details(id = "id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="asmi",mailid="asmi@gmail.com")
Details(id=30,name="ramesh",mailid="ramesh@gmail.com")
Details(30,"rajani","rajani@gmail.com")
Details("cherry","cherry@gmail.com",15)
Details(name="Remo",mailid="remo@gmail.com",id=2)'''




#employee task

''''def employedetails(name,salary,designation):
    print(name,salary,designation)

employedetails(name="arshi",salary = 12345,designation="developer")
employedetails("Asmi",12345,"frontend developer")
employedetails(name="ramesh",salary = 2800000,designation="four man")
employedetails(salary = 23212122,designation="developer",name="remo")
'''


#defaul arguments

'''def grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("rice",1800)'''



'''def grocery(item="sugar",price=100):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery()'''


'''def grocery(item,price=200):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("ghee")'''


'''def grocery(item="dall",price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery(500)'''


#bakary->cake,price,qty

'''def bakary(cake,price,qty):
    print("cake %s"%cake)
    print("price %d"%price)
    print("quantity %.2f"%qty)
bakary("choclate",800,1.5)'''

'''def bakary(cake="black forst",price=12000,qty=2000):
    print("cake %s"%cake)
    print("price %d"%price)
    print("quantity %.2f"%qty)
bakary()'''

'''def bakary(cake,price,qty=800):
    print("cake %s"%cake)
    print("price %d"%price)
    print("quantity %.2f"%qty)
    
bakary("choclate",800)'''


'''def bakary(cake="red velvet",price,qty):
    print("cake %s"%cake)
    print("price %d"%price)
    print("quantity %.2f"%qty)
    
bakary(800,1.5)'''



# * arguments-> * is used to unpack the elements

'''a=[2,3,4,5,6]
print(a)
print(*a)'''

'''b=(5,6,7,8,9)
print(b)
print(*b)'''


'''a={8,9,10,11,12}
print(a)
print(*a)'''

'''d = {"name":"arshi","yaer":2026}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7
print(a)
print(b)
print(c)'''#error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7
print(a)
print(b)
print(*c)'''

'''a,*b,*c=2,3,4,5,6,7
print(a)
print(*b)
print(*c)'''#error

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error


'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''


'''a,b,c="cod"
print(a)
print(b)
print(c)'''


#veriable length arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
b=[1,2,3,4,5,6]
check(*b)
c=(1,2,3,4,5)
check(*c)
d={2,3,4,5,6}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''



'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
        

check1()
check1(2,3,4,5,6,7)
check1(2,3,4,4.4,4.6,2.2)
check1(2,3,4,5.5,6.2,"Arshi")
check1(2,3,4,5.5,6.2,"Arshi",3+5j,True,False)'''


#kwarfs(**)

'''def details(**a):
    print(a)
    print(type(a))
details()
d = {"names":["Arshi","Himaja","pooja"],"marks":[90,80,100],"status":["p","a","p"]}
details(**d)
'''

'''def details(**a):
    print(a)
    print(type(a))

    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d = {"names":["Arshi","Himaja","pooja"],"marks":[90,80,100],"status":["p","a","p"]}
details(**d)'''





#both * and **
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,3.5,2.5)
final(*data)
details={"name":["Arshi","sweety","manu"],"marks":[90,80,100]}
final(**details)
final(*data,**details)'''



#global and local variables (also called as scope variabes)
#first case of global variable

'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''


#second case of global variable
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''


#third case of global and local variable

'''a=3
def check():
    a=5
    print("inside value is",a)
    a=10
    print("updated value is",a+5)

    b=12 #Local variable
    b=b+a
    print("local value is",b)
check()
print("outside value is",a)
print("outside value is",b)'''


#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13
    b=b+a
    print("b value is",b)

final()
print("a value is",a)
print("b value is",b)'''




#chr,ord
#ASCII
'''print(chr(65))

print(chr(90))

print(chr(92))

print(ord("a"))

print(ord("z"))'''

#print(ord(98))
#print(chr("a"))

'''
for i in range(65,91):
    print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input("Enter your name")

for i in a:
    print(i,":",ord(i))'''



    























































































