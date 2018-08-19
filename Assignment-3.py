1>>creating list with user defined input:-
w=[]
q=int(input("enter how many element you want in list"))
for i in range(q):
    x=int(input("enter 1 for number,enter 2 for string"))
    if x==1:
            c=int(input("enter number"))
            w.append(c)
    elif x==2:
            v=input("enter string")
            w.append(v)
    else :
            print("enter a valid choice")
            break
print(w) 

2>>creating list with user defined input:-
w=[]
q=int(input("enter how many element you want in list"))
for i in range(q):
    x=int(input("enter 1 for number,enter 2 for string"))
    if x==1:
            c=int(input("enter number"))
            w.append(c)
    elif x==2:
            v=input("enter string")
            w.append(v)
    else :
            print("enter a valid choice")
            break
print(w)          
b=["google","apple","facebook","microsoft","tesla"]
w=w+b
print(w)


3>>Count the number of time an object occurs in a list:-
a=[]
b=int(input("Enter the size of list "))
for i in range(b):
    c=input("Enter object ")
    a.append(c)
c=input("Enter object which you want to find its times of occurence ")
print(a.count(c))

4>>creating a list with number and sorting in ascending order:-
v=int(input("enter the size of the list:-"))
w=[]
for i in range(v):
                c=int(input("enter no"))
                w.append(c)
print(w)
print("after sorting")
w.sort()

5>>Creating array  c and appending array a and b in it and sorting it in ascending order:-
x=[2,3,5,7,8,50]
y=[9,11,21,30,54,66]
c=[]
z=x+y
z.sort()
print(z)

6>>count even and odd no in a list:-
x=[1,2,25,56,89,41,52,48,96]
print(x)
count=0
y=0
for i in x:
    if i%2==0:
        count=count+1
    else:
        y=y+1
print("even no in list =",count)
print("odd no in list =",y)

7>>Print a tuple in reverse order:-
x=[]
y=int(input("Enter the size of tuple\n"))
print("Enter elements")
for i in range(y):
    z=int(input())
    x.append(z)
tup=tuple(x)
print("Tuple is : " , tup)
rev=reversed(tup)
print("Reversed tuple is : " , tuple(rev))
