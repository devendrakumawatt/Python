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