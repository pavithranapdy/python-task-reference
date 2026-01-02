#A Python decorator is a way to add extra functionality to a function without changing its code. Think of it as wrapping a function with another function.

def my_decorator(func):  # my_decorator is decorator & func is argument
    def wrapper():        # wrapper is nexted function
        print("Before function execution")
        func()          # call the original function say_hello
        print("After function execution\n")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()         # function call


#Decorator with Arguments
def my_decorator(func):
    def wrapper(name):
        print("Function is starting")
        func(name)
        print("Function is ending")
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Alice")