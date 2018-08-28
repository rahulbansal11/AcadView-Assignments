1>>Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class:-
pi = 3.14
class circle:
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return pi * (self.radius**2)
    def getCircumference(self):
        return 2 * pi * self.radius
c1 = circle(int(input("Enter radius of circle ")))
print("Area is {}".format(c1.getArea()))
print("Circumference is {}".format(c1.getCircumference()))


2>>Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student:-
class Student:
    def __init__(self):
        self.name = input("Enter name:-")
        self.roll = int(input("Enter roll number:-"))
    def display(self):
        print("Name is " , self.name)
        print("Age is ",self.age)
        print("Roll number is ",self.roll)
        print("Marks are ",self.marks)
    def setAge(self,sage):
        self.age = sage
    def setMarks(self,marks):
        self.marks = marks
s1 = Student()
s1.setAge(int(input("Enter age:-")))
s1.setMarks(int(input("Enter marks:-")))
s1.display()


3>>Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius:-
class Temperature:
    def convertFahrenheit(self):
        self.celsius = float(input("Enter temperature in celcius "))
        self.fahrenheit = ((9/5) * self.celsius) + 32
        print("Temperature in fahrenheit is ",self.fahrenheit)
    def convertCelsius(self):
        self.fahrenheit = float(input("Enter temperature in fahrenheit "))
        self.celsius = (5/9) * (self.fahrenheit - 32)
        print("Temperature in celsius is ",self.celsius)
t1 = Temperature()
t1.convertFahrenheit()
t1.convertCelsius()


4>>Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details:-
class MovieDetails:
    def __init__(self,an,yr,ra):
        self.artistname = an
        self.year = yr
        self.ratings =ra 
    def display(self):
        print("Name of artist is ",self.artistname)
        print("Year of release is ",self.year)
        print("Ratings are ",self.ratings)
    def add(self):
        self.artistname = input('Enter artist name:- ')
        self.year = int(input('Enter year of release:-'))
        self.ratings = float(input('Enter ratings:-'))
arti=' '
ye=0
ra=0
m = MovieDetails(arti,ye,ra)
m.add()
m.display()


5>>Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method:-
class Animal:
    def animal_attribute(self):
        print("Animal class")
class Tiger(Animal):
    def animal_attribute(self):
        super().animal_attribute()
        print("Tiger class")
T1 = Tiger()
T1.animal_attribute()


6>>What will be the output of following code:-
class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

    class B(A):
        def g(self):
            return 'B'

    a = A()
    b = B()
    print a.f(), b.f()
    print a.g(), b.g()

OUTPUT is:- A B

7>>Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area:-
class Shape:
    def __init__(self,l,b):
        self.leng = l
        self.bre = b
    def area(self,l,b):
        self.leng = l
        self.bre = b
        return self.leng*self.bre
class rect(Shape):
    def __init__(self,l,b):
        self.leng = l
        self.bre = b
class squ(Shape):
    def __init__(self,s):
        self.side = s
    def area(self):
        return self.side*self.side
print("Rectangle")
l = int(input("Enter length:-"))
b = int(input("Enter breadth:-"))
r = rect(l,b)
print(r.area(l,b))
print("Square")
s = int(input("Enter side:="))
s = squ(s)
print(s.area())
