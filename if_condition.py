#if condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")'''


'''a=40
b=60
if a>b:
    print("less")'''


'''a=50
b=80
if b>a:
    print("greater")'''


'''a=5
b=9
if a<=b:
    print("true")'''

'''a=11
b=13
if b>=a:
    print("greater")'''

'''a=5
b=5
if a==b:
    print("equal")'''


'''a=3
b=5
if a!=b:
    print("not equal")'''

'''a = int(input())
b = int(input())
if a<b:
    print("Less")'''

'''a = int(input())
if a>30:
    print("greater")'''

'''a="python"
if a=="python":
    print("true")'''

'''a="java"
if a=="python":
    print("false")'''


#if condition by using logical operators
#and,or,not

'''a=4
b=8
if a<b and b>a:
    print("less")'''


'''a=6
b=9
if a<=b and b>=a:
    print("true")'''

'''a=7
b=10
if a!=b and b!=a:
    print("ture")'''

'''a=8
b=8
if a==b and b!=a:
    print("True")'''

'''a=4
b=8
if a!=b or b==a:
    print("less")'''

'''a=4
b=8
if a<b or b>a:
    print("less")'''

'''a=4
b=8
if a<=b and b>=a:
    print("less")'''

'''a=4
b=8
if a<b and b>a:
    print("less")'''


'''a=4
b=8
if not a<b:
    print("True")'''

'''a=4
b=8
if not a>b:
    print("false")'''

'''a=4
b=8
if not a>b and b>a:
    print("true")'''

'''a=int(input())
b=int(input())
if not a>b:
    print("false")'''

'''a=int(input())
b=int(input())
if not a>b and b>a:
    print("false")'''


'''a=int(input())
b=int(input())
if a<b and b>a:
    print("greater")'''


    
#if condition by using Identify operators
#is,is not

'''a=10
if type(a) is int:
    print("it is int")'''

'''a=10
if type(a) is not int:
    print("false")'''

'''a=10.5
if type(a) is not int:
    print("it is not int")'''

'''a=int(input())
if type(a) is int:
    print("it is int")'''

#if condition by using membership operators
#in,not in
'''a =[2,3,4,5,6,7,9,10]
if 10 in a:
    print("true")'''

'''a =[2,3,4,5,6,7,9,10]
if 10 not in a:
    print("false")'''

'''a =[2,3,4,5,6,7,9,10]
if 15 not in a:
    print("false")'''

'''a =int(input())
if 30 in a:
    print("true")'''#error


'''a =[2,3,4,5,6,7,9,10]
b = int(input())
if b in a:
    print("true")'''

#if-else condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a>b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a>=b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a!=b:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a==b:
    print("true")
else:
    print("false")'''

#if-else condition by using logical operators
#and,or,not

'''a=10
b=20
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a>b and b<a:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if a>b or b<a:
    print("true")
else:
    print("false")'''

'''a=10
b=20
if not a<b:
    print("true")
else:
    print("false")'''


#if-else condition by using Identify operators
#is,is not

'''a=10
if type(a) is int:
    print("it is int")
else:
    print("not int")'''

'''a=10.5
if type(a) is int:
    print("it is int")
else:
    print("not int")'''

'''a=10
if type(a) is not int:
    print("it is int")
else:
    print("is int")'''

#if-else condition by using membership operators
#in,not in

'''a =[2,3,4,5,6,7,9,10]
if 10 in a:
    print("true")
else:
    print("false")'''

'''a =[2,3,4,5,6,7,9,10]
if 15 in a:
    print("true")
else:
    print("false")'''

'''a =[2,3,4,5,6,7,9,10]
if 10 not in a:
    print("true")
else:
    print("false")'''




#if-elif-else condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=5
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=9
b=12
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''


'''a=5
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
elif b!=a:
    print("not equal")
else:
    print("true")'''

#if-elif-else condition by using logical operators
#and,or,not

'''a=9
b=12
if a<b and b>a:
    print("less")
elif a>b or b>a:
    print("greater")
elif not a>b:
    print("greater")
else:
    print("true")'''



#if-elif-else condition by using Identify operators
#is,is not

'''a=9
b=12
if type(a) is int:
    print("true")
elif type(a) is not int:
    print("false")
else:
    print("true")'''



#if-elif-else condition by using membership operators
#in,not in

'''a =[2,3,4,5,6,7,9,10]
if 10 in a:
    print("true")
elif 1 not in a:
    print("false")
else:
    print("false")'''




#multiple if condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("true")'''



'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("true")'''

'''a=2
b=4
if a>b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("true")'''


#multiple ife condition by using logical operators
#and,or,not

'''a=9
b=12
if a<b and b>a:
    print("less")
if a>b or b>a:
    print("greater")
if not a>b:
    print("greater")'''




#if-elif-else condition by using Identify operators
#is,is not

'''a=9
b=12
if type(a) is int:
    print("true")
if type(a) is not float:
    print("false")'''



#if-elif-else condition by using membership operators
#in,not in

'''a =[2,3,4,5,6,7,9,10]
if 10 in a:
    print("number in a")
if 1 not in a:
    print("number not in a")'''




#nested-if comparision operators

'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a<b:
    print("less")
if b>a:
    print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''



'''a=6
b=12
if a>b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a<b:
    print("less")
    if b==a:
        print("greater")'''


'''a=6
b=12
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''



'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''


'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

    



#nested-if condition by using logical operators
#and,or,not

'''a=9
b=12
if a<b and b>a:
    print("less")
    if a<b or b>a:
        print("greater")
    elif not b>a:
        print("greater")
    else:
        print("false")'''




##nested-if condition by using Identify operators
#is,is not

'''a=9
b=12
if type(a) is int:
    print("true")
    if type(a) is not float:
        print("false")
    else:
        print("false")'''



##nested-if condition by using membership operators
#in,not in

a =[2,3,4,5,6,7,9,10]
if 10 in a:
    print("number in a")
    if 1 not in a:
        print("number not in a")


























