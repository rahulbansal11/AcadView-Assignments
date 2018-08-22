1>>Take an input year from user and decide whether it is a leap year or not:-
x=int(input("Enter an year\n"))
if x % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


2>>Take length and breadth input from user and check whether the dimensions are of square or rectangle:-
x= float(input("Enter length "))
y= float(input("Enter breadth "))
if x == y:
    print("It's a Square")
else:
    print("It's Rectangle")


3>>Take the input age of 3 people and determine oldest and youngest among them:-
x = int(input("Enter age of first person "))
y = int(input("Enter age of second person "))
z = int(input("Enter age of third person "))
l,g = 0,0
if x > y and x > z:
    g = x
    if(y<z):
        l = y
    else:
        l = z
elif y > x and y > z:
    g = y
    if x < z:
        l = x
    else:
        l = z
else:
    g = age3
    if x < y:
        l = x
    else:
        l = y
print("Oldest one is with age of " , g)
print("Youngest one is with age of" , l)


4>>Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service
1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR"  :-

age = int(input("Enter age "))
sex = input("Enter sex (M or F) ")
mar = input("Enter marital status ( Y or N ) ")
if age >= 20 and age <= 40:
    if sex == 'F':
        print("Place of Service is Urban Areas")
    elif sex == 'M' and age >= 20 and age < 40:
        print("Place of Service is Anywhere")
    elif sex == 'M' and age >=40 and age < 60:
        print("Place of Service is Urban Areas")
else:
    print("Error")


5>>A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user:-
x = int(input("Enter quantity of Item "))
total = x * 100 #100 is cost of 1 unit
if total > 1000:
    total = total - ( ( total * 10) / 100 )
print("Total price: " , total)


*----------------------*-----------------------*---------------------*----------------------*----------------------------*---------------------*----------------------------*-----------------------*
1>>Take 10 integers from user and print it on screen:-
x = []
print("Enter elements")
for i in range(10):
    n = int(input())
    x.append(n)
for i in range(10):
    print(x[i] , end=' ' )


2>>Write an infinite loop.An infinite loop never ends. Condition is always true:-
while True:
    print("infinite loop")


3>>Create a list of integer elements by user input. Make a new list which will store square of elements of previous list:-
a = []
print("\nEnter elements within the size of 10:-")
for i in range(10):
    n = int(input())
    a.append(n)
print("List is " , a)
b = list(x**2 for x in a)
print("List with square of elements from entered list " , b)


4>>From a list containing ints, strings and floats, make three lists to store them separately:-
x = [1,15.4,"Rahul",1,545,8856,22.25,245.245,"Acadview"]
Intlist = []
Strlist = []
Flolist = []
for i in x:
    if(isinstance(i,int)):
        Intlist.append(i)
    elif(isinstance(i,float)):
        Flolist.append(i)
    elif(isinstance(i,str)):
        Strlist.append(i)
print("List is : " , x)
print("List with integers is : " , Intlist)
print("List with floats is : " , Flolist)
print("List with strings is : " , Strlist)


5>>Using range(1,101), make a list containing only prime numbers:-
x = 0
y = []
for i in range(1,101):
    x = 0
    for j in range(2,i):
        if i % j == 0:
            x = 1
            break;
    if x == 0:
        y.append(i)
print(y)


6>>Print the following patterns:-
* 
** 
*** 
****
for i in range(5):
    for j in range(i):
        print("*",end='')
    print("\r")


7>>Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop:-
x=[]    
f=int(input("Enter size of list:-"))
for i in range(f):
    t=int(input("Enter elements:-"))
    x.append(t)
print(x)
j=int(input("Enter element you want to delete from list:-"))
for i in x:
    if i==j:
        x.remove(i)
print(x)
