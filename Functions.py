# Functions in python -

# In-Built Function -
print("Hello World!")

# User-Defined Functions -
def greet() :
    print("Hello Learner!")

greet()

# Function with parameters and arguments -
def add(a, b) :            # a and b are parameters
    return a + b

sum = add(3, 5)            # 3 and 5 are arguments
print(sum)


# positional arguments -
def marks(a, b, c) :
    return a + b + c

result = marks(23, 45, 50)    
        # 'a' take '23' , 'b' take '45' , 'c' take '50'
print(result)

# default arguments -
def greet(name = "Guest") :
    print(f"Hello {name}!")

greet()             # uses default value 'Guest'
greet("Devendra")   # uses argument value "Devendra"


# keyword arguments -
def intro(name, age) :
    print(f"My name is {name} and I am {age} years old.")

intro(age = 24, name = "Dev")