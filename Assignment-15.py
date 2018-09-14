1>>Write a python script to create a databse of students named Students:-
import sqlite3
db1=sqlite3.connect('Students.db')
print("DataBase Created")
db1.close()


2>>Take students name and marks(between 0-100) as input from user 10 times using loops:-
list=[]
for i in range(10):
    x=input("enter name of student:-")
    y=int(input("enter no from 1-100:-"))
    if y>100 or y<1:
        print("enter a valid no")
        i=i-1
    else:
        z=x,y
        list.append(z) 


3>>Add these values in two columns named "Name" and "Marks" with the appropriate data type:-
import sqlite3

try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query="insert into Students(name,marks)values(?,?)"
    record = list
    cursor.executemany(query,record)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Pr
              oblem occured: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("DONE")  


4>>Print the names of all the students who scored more than 80 marks:-
import sqlite3
try:
    con = sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='select * from Students where marks>80'
    cursor.execute(query)
    data=cursor.fetchall()
    for a in data:
        print('Name:{}'.format(a[0]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("problem occured",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Done")  
