# class Sample:
#     s=4 #This is attribute
#     def hello(self): #This is method
#         print("Helloo")
#     print("I am initialized")
# print(Sample().s)
# print(Sample().hello())
# obj = Sample()
# print(obj.s)
# obj.hello()
# Constructor will accept the parameters instead of class

# class Factory:
#     def __init__(self,material,zips,pockets): # constructor
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets
#         pass
#     def show(self):
#         print(f"Your materials are {self.material}, {self.pockets} {self.zips}")

# comp=Factory('leather',2,3)
# cmp2=Factory('silk',3,2)
# print(comp.pockets)

# class Animal:
#     # class attribute
#     new_animal='Lion'
#     #instance method since it have self defined
#     def __init__(self,age):
#         #instance attribute
#         self.age=age 
#         pass
#     # self targets instance location and variable also since whole calling with object object always works as a argument so we define it as self
#     def show(self):
#         print("Welcome to the Class")

#     @classmethod
#     #cls targets class location 
#     def hello(cls):
#         print("Hello Brother")
#     @staticmethod
#     # a normal function placed in class
#     def static(): 
#         print("Namaster")

# obj=Animal()
# # it is not targeting cls in hello function
# obj.hello()

# -------INHERITANCE----------
# class Parent:
#     fa="I am attribute "
#     def hello(self):
#         print("Hello it's me your parent")

# class Child(Parent):
#     pass

# call=Child()
# call.hello()
# print(call.fa)

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         pass
#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#             print(f"Hello your name is {self.name} {self.age}")
#     pass

# person1=Animal("Sneha")
# person2=Human("Sneha",22)
# person1.show()
# person2.show()
# -------------MULTIPLE INHERITANCE----------------
# class Animal:
#    def __init__(self,name):
#        pass
# class Human:
#     def __init__(self,name, age):
#         pass
# class Robo(Animal,Human):
#     name3="charlie"
# obj=Robo() # Will follow constructor of first parent called as method resolution order MRO
# ----------MULTILEVEL INHERITANCE--------
# class Factory:
#     def __init__(self,material, zip):
#         self.material=material
#         self.zip=zip
        
# class Factory2(Factory):
#     def __init__(self, material, zip, Pockets):
#         super().__init__(material, zip)
#         self.Pockets=Pockets

# class Factory3(Factory2):
#     def __init__(self, material, zip, Pockets,Color):
#         super().__init__(material, zip, Pockets)
#         self.Color=Color

# obj=Factory3()

#-----------------POLYMORPHISM-----------
# Same name different forms
# def show():
#     print("Show 1")
# def show():
#     print("Show 2")

# class Animal():
#     def show(self):
#         print("Hello this is me Animal")

# class Human(Animal):
#     def show(self):
#         print("It's me human")
# obj=Human()
# obj.show()# This is method overriding: Child class and parent both have same name of function so show will run for child class as the parent function data will be over rided on it  
# Method Over riding is achieved through Inheritance
# Mehtod Overloading is not supported in Python as it overwrite the Data

# -----------DUCK TYPING------ to achieve Polymorphism
# class Animal:
#     def show(self):
#         print("I am Animal")
# class Human:
#     def show(self):
#         print("I am Human")

# obj1=Animal()
# obj2= Human()
# obj1.show()
# obj2.show()


# --------------ENCAPSULATION--------------------------
# Access Modifiers
# single underscore: Protected (Python doesn't support just for understanding)
# doubkle underscore: Private Can't be accesed outside class
# class Factory:
#     __a="Pune"
#     def __show(self):
#         print("Hello this company is Pune Company")
# class Bhopal(Factory):
#     def show2 (self):
#         print(super().a)
# obj=Factory()
# obj2=Bhopal()
# obj2.show2()
# ------------------ABSTRACTION--------------
# Doesn't exist in Python but could be achieved using it's library
# Abstrction is used to setup rules
# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side=side

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius=radius

#     def perimeter(self):
#         print("I exists")

#     def area(self):
#         print ("I exists")

# obj=Circle(3)
# obj=Square()

# ---------------DUNDER METHODS---------
# Start and end with double underscores
# Gets self called

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def __str__(self):
#         return (f"Hello I am {self.name}")
#     def __add__(self, other):
#         return (f"Sum of your age is {self.age+other.age}")

# obj=Animal("Sneha",12)
# obj2=Animal("Rahul",12)
# print(obj+obj2)