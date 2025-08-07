# Example of abstraction
from abc import ABC, abstractmethod
class Teahouse(ABC):
    def processCompleted(self):
        self.order()
        self.addingMaterials()
        self.serve()
    @abstractmethod
    def order(self):
        pass
    @abstractmethod
    def addingMaterials(self):
        pass
    @abstractmethod
    def serve(self):
        pass
class milkTea(Teahouse):
     def order(self):
        print("Ordering milk tea")

     def addingMaterials(self):
        print("Adding milk tea materials")
    
     def serve(self):
        print("Serving milk tea")
        
        
class blackTea(Teahouse):
    def order(self):
        print("Ordering black tea")

    def addingMaterials(self):
        print("Adding black tea materials")

    def serve(self):
        print("Serve black tea materials")
        
user1= milkTea()
user1.processCompleted()
user2= blackTea()
user2.processCompleted()

# Polymorphism ->
# Polymorphism is the ability of an object to take on multiple forms. This is achieved by writing methods that are common to all objects of a class and its subclasses.
# In Python, polymorphism is achieved through method overriding and method overloading.
# Method overriding: When a subclass provides a different implementation of a method that is already defined in its

class Human:
    def walk(self):
        print("Walk with 2 legs")

class Lion:
    def walk(self):
        print("Walk with 4 legs")

class Dog:
    def walk(self):
        print("Walk with 4 legs")

obj1 = Human()
obj2 = Lion()
obj3 = Dog()

for i in [obj1, obj2, obj3]:
    i.walk()

