1>>Create a function to calculate the area of a sphere by taking radius from user:-
pi = 3.14
def area(rad):
    return 4 * pi * (r**2)
r = int(input("Enter radius of sphere\t"))
print(area(r))


2>>Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3]:-
list = []
def perfect(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0 :
            sum += i
    return sum
for j in range(1,1000):
    s = perfect(j)
    if s == j :
        print(j)


3>>Print multiplication table of n using loops, where n is an integer and is taken as input from the user:-
def mulTable(n):
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
find = int(input("Enter a number whose table you want\t"))
mulTable(find)


4>>Write a function to calculate power of a number raised to other ( a^b ) using recursion:-
def pow(a,b):
    if b == 0:
        return 1
    else:
        return a * pow(a,b-1)
num = int(input("Enter a number whose power you wanna find\t"))
pp = int(input("Enter what power you want it raised\t"))
print(pow(num,pp))
