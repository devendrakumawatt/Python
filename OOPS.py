# OOPS in python -

# class 
class Animal :
    name = "Cat"     # Attribute

    def sound(self) :  # Method
        print("Meoowwwww!")

# Accessing the attributes and methods 
print(Animal().name)
Animal().sound() 

# Creating object -
a = Animal()     # 'a' is an object
print(a.name)    # Accessing attribute using object
a.sound()        # Accessing method using object


# contructor - 
class Student :
    def __init__(self, name, age) :  # Constructor
        self.name = name
        self.age = age

    def show(self) :
        print(f"Name : {self.name} and age : {self.age}")


s1 = Student("Devendra" , 24)
s1.show()


# Attribute types [Class, Instance] -
class Family :
    head = "PAPA"     # Class Attribute

    def totalMember(self, members) :
        self.members = members      # Instance Attribute
        print(f"Total members : {self.members}")


# Method Types [Instance, Class, Static] -

# Instance Method -
class MyClass :
    def instance_method(self) :
        print("This is an instance method")


# Class Method -
class MyNewClass :
    @classmethod
    def class_method(cls) :
        print("This is a class method")


# Static Method -
class NewClass :
    @staticmethod
    def static_method() :
        print("This is a static method")



# Inheritance -
class Parent :
    def speak(self) :
        print("Parent speaking")

class Child(Parent) :
    pass

c = Child()
c.speak()


# Constructor in Inheritance -
class Parent :
    def __init__(self, name) :
        self.name = name

class Child(Parent) :
    pass

c = Child("Devendra")
print(c.name)


# use of super ---
class Parent :
    def __init__(self, name) :
        self.name = name

class Child(Parent) :
    def __init__(self,name, age) :
        super().__init__(name)
        self.age = age

p = Parent("Dada")
print(p.name)
c = Child("baby", 12)
print(f"name : {c.name} , age : {c.age}")


# Types of Inheritence [Single, Multiple, Multilevel] -

# Single Inheritance -
class Parent :
    def speak(self) :
        print("Parent speaking")

class Child(Parent) :
    pass

c = Child()
c.speak()

# Multiple Inheritance -
class Father :
    def __init__(self, name):
        self.name = name

class Mother :
    def __init__(self, age) :
        self.age = age

class Child(Father, Mother) :
    pass

obj = Child("Devendra")
print(obj.name)


# Multilevel Inheritance -
class Grandparent : 
    def __init__(self, name) :
        self.name = name

class Parent(Grandparent) :
    def __init__(self, name, age) :
        super().__init__(name)
        self.age = age

class Child(Parent) :
    def __init__(self,name, age, city) :
        super().__init__(name, age)
        self.city = city

obj = Child("Dev", 24, "Sikar")
print(f"Name : {obj.name} , Age : {obj.age} , City : {obj.city}")