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