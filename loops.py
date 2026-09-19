#loops
#for,while,range,break,continue,pass

#for loop()

'''a=[10,20,30,40,50]
for i in a:
    print(i)'''


'''a=[10,20,30,40,50]
for i in a:
    print(a)'''



'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))'''



'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={4,5,6,7,8}
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a=(4,5,6,7,8)
for i in a:
    print(i)
print(type(a))
print(type(i))'''



'''a={"year":2026,"month":"sep","date":16}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
    
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[1,2,4,5,6]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[1.5,2.3,4.5,5.6,6.7]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=["Python","c"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4+2j,5+6j]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[1,2.5,"Arshi",4+5j,True,False]
print(type(a))
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''




'''a=["apple","Banana","grapes"]
#["APPLE",BANANA","GRAPES"]
print[a.upper()]'''







#attendance tracker
'''while True:
    students=int(input("enter the total no.of students"))
    p=0
    a=0
    for i in range(1,students+1):
        attendence = input(f"students {i} (p/a)")
        if attendence=="p":
            p+=1
        elif attendence=="a":
            a+=1

    print("......Attendence Tracker.........")'''



    print("total no of students",students)
    print("total no of presenties",p)
    print("total no of absenties",a)

