1>>Write a python script to create a databse of students named Students:-
import pymongo
client=pymongo.MongoClient()
data=client['Students']
collection=data['students_collection']


2>>Take students name and marks(between 0-100) as input from user 10 times using loops

3>>Add these values in two columns named "Name" and "Marks" with the appropriate data type:-
for i in range(0,10):
    name=input('Enter name:-')
    marks=int(input('Enter marks:-'))
    collection.insert_one({'Name':name,'Marks':marks})
d = collection.find()
for a in d:
    print(a)


4>>Print the names of all the students who scored more than 80 marks:-
b=collection.find({"Marks":{"$gt":80}})
for i in b:
    print(i)
