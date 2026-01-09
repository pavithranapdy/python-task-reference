# #A Python decorator is a way to add extra functionality to a function without changing its code. Think of it as wrapping a function with another function.
# print("1. Decorator using @ symbol")
# def my_decorator(func):  # my_decorator is decorator & func is argument
#     def wrapper():        # wrapper is nexted function
#         print("Before function execution")
#         func()          # call the original function say_hello
#         print("After function execution\n")
#     return wrapper

# @my_decorator           #say_hello = my_decorator(say_hello)
# def say_hello():
#     print("Hello!")

# say_hello()         # function call


# #Decorator with Arguments
# print("2. Decorator using @ Passing Function as argument")
# def my_decorator(func):
#     def wrapper(name):
#         print("Function is starting")
#         func(name)
#         print("Function is ending")
#     return wrapper

# @my_decorator
# def greet(name):
#     print("Hello", name)

# greet("Alice")

# print("\n3. Decorator using @ Passing Function as argument & if cond.")
# def check_positive(func):   # 2. called, func refer original Square fun
#     def wrapper(x):         # 3. wrapper func is created (not executed)
#         if x < 0:           # 6. inside wrapper(5)
#             print("Negative number not allowed")
#             return
#         return func(x)      # 7. return or call original Square fun
#     return wrapper          # 4. wrapper is returned

# @check_positive       # 1. Py read the decorator, it does not wait until the square is called
# def square(x):         # 5. call square(5)
#     print(x * x)        # 8. original square(5) is execute
# x=int(input("enter any no "))
# square(x)


# print("3.Real Time Example using decorator @")
# import random
# def login_required(func):
#     def wrapper(username, userpassword):
#         name = "pavithran"
#         password = "123456"

#         if username == "" or userpassword == "":
#             print("Username or password cannot be empty")
#         elif username == name and userpassword == password:
#             func(username)
#         else:
#             print("Access denied")
#     return wrapper


# @login_required
# def dashboard(username):
#     print("Login successful")
#     print("Welcome to dashboard,", username)
#     otp = random. randint(1000, 9999)
#     print("Your OTP is:", otp)


# # User input
# username = input("Enter username: ")
# userpassword = input("Enter password: ")

# dashboard(username, userpassword)

print(".Multiplication table of 7 till 7 x 5 = 35")
def my_decorator(func):
    def wrapper(x, y):
        print("Table of 7")
        func(x, y)
        print("Done")
    return wrapper

@my_decorator   
def multiple(x, y):
    for i in range(x, y):
        print("7 x", i, "=", 7 * i)
x=int(input("enter first no "))
y=int(input("enter last no "))
multiple(x, y)
