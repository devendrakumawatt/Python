# Decorator in python -

def my_decorator(func) :
    def wrapper() :
        print("This is before function hello.")
        func()
        print("This is after function hello.")
    return wrapper


@my_decorator
def hello() :
    print("This is hello function.")

hello()


# *args /**kwargs in python -
def new_func(*args, **kwargs) :
    print("args : ", args)
    print("kwargs : ", kwargs)

new_func(12,34,12,name = "Dev", age = 24)


# use of *args / **kwargs with decorator in python -
def my_decorator(func) :
    def wrapper(*args , **kwargs) :
        print("This is before function hello.")
        func(*args , **kwargs)
        print("This is after function hello.")
    return wrapper


@my_decorator
def addition(*args, **kwargs) :
    print("This is Addition function.")
    print("args : ", args)
    print("kwargs : ", kwargs)

addition(12,34,12, name = "dev", age = 24)


