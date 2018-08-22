1>>Reverse the whole list using list methods:-
x=[]
n=int(input("Enter size of list\n"))
print("Enter elements")
for i in range(n):
    y=int(input())
    x.append(y)
x.reverse();
print(x)


2>>Print all the uppercase letters from a string:-
string1=input("Enter a string\n")
string2=" "
for i in range(len(string1)):
    if string1[i].isupper():
        string2 += string1[i] + " "
print(string2)


3>>Split the user input on comma's and store the values in a list as integers:-
'''x=int(input("Enter number of inputs\n"))
y=[int(input()) for i in range(n)]
print(y)'''
z=list(map(int,input().split(',')))    
print(z)


4>>Check whether a string is palindromic or not:-
str1=input("Enter a string you wanna check\n")
str2=str1[::-1]
if str1==str2:
    print("%s is palindromic" %(str1))
else:
    print("%s is not palindromic" %(str1))


5>>Make a deepcopy of a list and write the difference between shallow copy and deep copy:-
#Deep Copy
lis1_=[1,2,3,4]
print("List 1 is ",lis1_)
lis2_=lis1_
print("List 2 is ", lis2_)
lis2_[0]='Hey'
print("Now list 2 is ",lis2_,"\nand list 1 is ",lis1_)

#Shallow Copy
import copy as c
lis_1=[1,2,[3,4],5]
print("List 1 is ",lis_1)
lis_2=c.copy(lis_1)
print("List 2 is ", lis_2)
lis_1[2][0]='Done'
print("Now list 2 is ",lis2_,"\nand list 1 is ",lis1_)
lis_1[1]='Changed'
print("List 1 is ",lis_1)
print("List 2 is ", lis_2)
