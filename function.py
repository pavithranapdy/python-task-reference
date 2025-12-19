# def myFun():            # function definition
#     print("function is working")

#     x = 10
#     y = 10
#     z = x + y
#     print(z)
# myFun()                 # function call


# # argument
# # parameter

# name = "demo user"
# def display(a):   # parameter
#     print(a)

# display(name)  # argument
# display("vidhya")

# a=int(input("enter the 1st Value"))
# b=int(input("enter the 2nd Value"))

# def operation(n1,n2):
#     print("sum of two value", n1+n2)

# operation(a,b)

# print("default arguments")
# def addition(a,b,c = 25): #c=25 value is not provided in the function call 
#     z = a + b + c
#     print(z) 
# addition(10,20)

# # values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
# print("Keyword Arguments") 
# def student(fname, lname):
#     print(fname, lname)

# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks')

# # Non-keyword arguments
# print("Non-Keyword Arguments i.e., *no") 
# def myFunction(x,*numbers): #share a no. of variables in function call(*no)
#     print(numbers)
#     print(x)

# myFunction(2,5,1,5,8.30,2)


# # keyword arguments
# print("Keyword Arguments i.e., **data") 
# def f2(**data):
#     # print(name,email)
#     print(data)

# f2(name = "aaa", email = "aaa@gmail.com")

# # function return
# print("return function")
# def f3(n1,n2):
#     print("demo")
#     return n1 + n2 # return statement ends a function and sends a value back to the caller

# print(f3(2,5))

# # scope defines the region of a program where a variable is accessible

# # local scope - variable defined inside a function/ fun. parameter also have local scope
# idNumber = 263546
# def f4():
#     idNumber = "ST001"
#     print(idNumber,"inside the function")

# f4()
# print(idNumber,"outside the function")



# # The global keyword is required if you want to modify or create a global variable from inside a function's local scope.

# x = 10 # Global variable

# def modify_global():
#   global x # Declare intent to modify the global variable
#   x = 20   # This modifies the global x

# modify_global()
# print(x) # Output: 20
