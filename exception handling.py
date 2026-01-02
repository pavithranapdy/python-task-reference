# # try: Runs the risky code that might cause an error.
# # except: Catches and handles the error if one occurs.
# # else: Executes only if no exception occurs in try.
# # finally: Runs regardless of what happens useful for cleanup tasks like closing files.
# print("Exception handling- Zerodivision error")
# try:
#     print("try block is running")
#     n = 0
#     res = 100 / n
    
# except ZeroDivisionError:
#     print("input value is 0 You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number!")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.\n")

# print("Exception handling- Value error")
# try:
#     print("try block is running")
#     x = int("str")
#     inv = 1 / x 
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number! str cannot be converted to an int ")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.\n")

# print("Exception handling- else")
# try:
#     print("try block is running")
#     res=10
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number! ")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.\n")
    
# print("Exception handling using function")
# def a():
#   a = ["10", "twenty", 30]  # Mixed list of integers and strings
#   print(a)
#   total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
# try:
#     print("try block is running")
#     a()   
   
# except (ValueError, TypeError) as e:
#     print("Error", e)
    
# except IndexError:
#     print("Index out of range.")



def divideNos(a, b):
  return a/b # An exception might raise here if b is 0 (ZeroDivisionError)
try:
   a = 20
   b = 0
   print('after division', divideNos(a, b)) 
   a = [1, 2, 3]
   print(a[3]) # An exception will raise here as size of array ‘a’ is 3 hence is accessible only up until 2nd index
 
# if IndexError exception is raised
except IndexError:            
   print('index error')
# if ZeroDivisionError exception is raised
except ZeroDivisionError as ex:
   print('zero division error',ex)


# Types of error
# print("1. Type error")
# a = 10
# b = "5"
# print(a + b)

# print("2. ValueError")
# num = int("abc")

# print("3. NameError")
# print(x)

# print("4. IndexError")
# numbers = [1, 2, 3]
# print(numbers[5])

# print("5. KeyError")
# data = {"name": "Alice"}
# print(data["age"])

# print("6. ZeroDivisionError")
# result = 10 / 0

# print("7. FileNotFoundError")
# file = open("myfile.txt")

# print("8. SyntaxError")
# if True
#     print("Hello")

# print("9. Importing a Non-Existing Module")
# import mymodule             #Importing a Non-Existing Module

# print("10. Importing a Wrong Name from a Module")
# from math import square     #math module does not have a function called square

# print("11. Correct Import (No Error)")
# from math import sqrt
# print(sqrt(16))