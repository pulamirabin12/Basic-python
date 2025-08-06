# Decorators
def exponents(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        return results**2
    return wrapper

@exponents
def calculate(a,b):
    return(a+b)

print(calculate(10,2))

#property -> use for the lastname and firstname = fullname

class Person:
    def __init__(self, firstname, lastname):
        self.firstname= firstname
        self.lastname= lastname

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
obj1 = Person("Rabin", "Magar")
print(obj1.firstname)
print(obj1.lastname)
print(obj1.fullname)

#4 pillars of oop-> Ecapsulation, Inheritance, Abstraction and polymorphism
#inheritance

class Parent:
    def __init__(self, lastname):
        self.lastname = lastname
    def hello(self):
        print("Hello from Parent class",self.lastname)

class Child(Parent):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        super().__init__(lastname)
    def hi(self):
        print("Hi from child class",self.firstname)
        super().hello()

obj2 = Child("Rabin","Magar")
obj2.hello()
obj2.hi()

''' wap to create a parent class named Classes with attribute like class_name section and have to inherit  it to child
 class named Students with attributes like name, age, and methods like study,
attend_class, and display_info using constructor and use super() to access parent class attributes and methods'''

'''class Classes:
    def __init__(self,class_name, section, ):
        self.class_name = class_name
    def name(self):
        print("")'''


#encapsulation in python
class Bank:
    def __init__(self,name , balance):
        self.name = name
        self.__balance = balance
    @property
    def getbalance(self):
        return self.__balance
    @getbalance.setter
    def setbalance(self,balance):
        self.__balance = balance

    def __calculateminbalance(self):
        return self.__balance> 500

user1 = Bank("Rabin", 1000)
print(user1._name)
print(user1.__balance) #1000
user1.setbalance = 2000
print(user1.getbalance)

#Abstraction in python ->hiding complex logic from user
from abc import ABC, abstractmethod
class Coffee(ABC):
    def makeCoffee(self):
        self.gason()
        self.addCoffee()
        self.addMaterials()
        self.servein()
    def makeCoffee(self):
        pass
    @abstractmethod
    def gason(self):
        pass
    @abstractmethod
    def addCoffee(self):
        pass
    @abstractmethod
    def addMaterials(self):
        pass
    @abstractmethod
    def servein(self):
        pass

class Espresso(Coffee):
    def gason(self):
        print("Coffee machine on")
    def addCoffee(self):
        print("addcoffee beans and extract it")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")
    
class Cappuccino(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("extracted coffee powder")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")

exp = Espresso()
exp.makeCoffee()

cap = Cappuccino()
cap.makeCoffee()


