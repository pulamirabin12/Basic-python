#OOP - object oriented programming
# programming paradigm based on the concept of program
# objects, which may contain data, in the form of fields (also known as attributes or property
# Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction, constructor, Decorators, magic/dunder
# Class - blueprint or template for creating objects
class Abc:
    # class attributes/properties/ methods and constructor
    name = "Ramden"
    age = 24
    gender = "male"
# this == self in python to refer to the instance of the class 
    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

    def add(seld,a,b):
        return a+b
# Object - instance of a class
obj = Abc()
print(obj.name)
obj.name = "hari"
print(obj.name) # hari
print(obj.age)
print(obj.gender)

# calling method
obj.printDetails() # Name: hari, Age: 24, Gender: male
print(obj.add(10,5)) # 15

two = Abc()
print(two.name) # Ramden    

# wap to create a class make Car with attributes like model, year, and methods like start, stop and display_info
class Car: 
    name = "Toyota"
    model = "Camry"
    year = 2020
    def start(self):
        return "Car started"
    def stop(self):
        return "Car stopped"
    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Name: {self.name}")
        # creating an object of the class
        car = Car()
        print(car.start()) # Car started
        print(car.stop()) # Car stopped
        car.display_info() # Model: Camry, Year: 2020, Name: Toyota
        # Inheritance - creating a new class from an existing class

                
    


#encapsulation = bundling data and methods that operate on that data
#inheritance = creating a new class that is a modified version of an existing class
#polymorphism = ability of an object to take on multiple forms
#4 pillers-> Encapsulation, Abstraction, Inheritance, Polymorphism 
# constructor
class Car: 
    def _init_(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        print("Car object created")
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Name: {self.name}")
        # creating an object of the class
        car = Car("Toyota", "Camry", 2020)
        car.display_info() # Model: Camry, Year: 2020, Name: Toyota
        car.start()
        car.stop() # Car stopped

        car2 = car("Nissan", "Magnite", 2021)
        car2.start() # Car started
        car2.stop() # Car stopped
        car2.display_info()

# wap to create a class named student with attributes like name, age, and methods like study, attend_class, and display_info using constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student object created")
    def study(self):
        print(f"{self.name} is studying")
    def attend_class(self):
        print(f"{self.name} is attending class")
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
student = Student("Rahul", 20)
student.display_info() # Name: Rahul, Age: 20
student.study() # Rahul is studying
student.attend_class() # Rahul is attending class
# Decorators in python -> @classmethod, @staticmethod, @property, @property.setter, @property.deleter, @property.getter

class Ones:
    two = "This is a class variable"

    #normal method
    def one(self):
        print("This is a method one {self.two}")


    #class method
    @classmethod
    def twos(cls):
        print(f"This is a class method {cls.two}")
    #static method
    @staticmethod
    def threes(a,b):
        print(f"This is a static method: {a+b}")
    
Ones.two()
Ones.three(10,20)

# wap to create a class named Student with attributes like name, age, and methods like study, attend_class, and display_info using constructor snd decorators
class Student:
    two = "This is a class variable"

    #normal method
    def name(self):
        print(f"This is a method one {self.two}")
    #class method
    @classmethod
    def age(cls):
        print(f"This is a class method {cls.two}")
    #static method
    @staticmethod
    def attend_class(a,b):
        print(f"This is a static method: {a+b}")
    
Student.two()
Student.name()
Student.age()


def add_five(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return wrapper
@add_five 
def add_number(a):
    return a

print(add_number(10))
