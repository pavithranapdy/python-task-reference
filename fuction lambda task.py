# # single argument function
# square = lambda x: x * x
# print("one argument function",square(5))  # Output: 25

# # multiple argument function
# add = lambda a, b: a + b
# print("multiple argument function",add(3, 4))  # Output: 7

# # filter function
# print("python program from a list using FILTER function")
# mylist = [3, 4, 5, 6, 44, 55, 22]
# print("My list= ", mylist)
# print()
# evenNos = filter(lambda x: x % 2==0, mylist)
# print("Even Nos in list",list(evenNos))

# oddNos = filter(lambda x: x % 2!=0, mylist)
# print("Odd Nos in list",list(oddNos))

# LargestNos = filter(lambda x: x >=50, mylist)
# print("print all Nos. greater than 50 in a list ",list(LargestNos))

# SmallestNos = filter(lambda x: x <=50, mylist)
# print("print all Nos. lesser than 50 in a list ",list(SmallestNos))
# print()
# #MAP function
# print("python program from a list using MAP function")

# square = map(lambda x: x **2, mylist)
# print("square",list(square))

# multiplyby2 = map(lambda x: x*2, mylist)
# print("multiply by 2",list(multiplyby2))

# sum= sum(map(lambda x:x*2, mylist))
# print("sum after multiply by 2 in list", sum)

# # reduce function

# from functools import reduce

# numbers = [1, 2, 3]

# result_with_initializer = reduce(lambda x, y: x + y, numbers, 100)
# print("redjuce function",result_with_initializer)

# # recursion function
# print("factorial using recursion function")
# n=int(input("enter any +ve single digit No."))
# def fact(n):
#   if n==0:
#     return 1
#   else:
#     return n * fact(n-1)

# # print("Factorial of ", n, "is", fact(n))
# print("1.Factorial using Recursive Function ")
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# print("2.Fibbonaci using Recursive Function ")
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2) #f(n)=f(n-1)+f(n-2)
# print(fibonacci(6))

# print("3.Sum of Natural using Recursive Function ")
# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n-1)

# print(sum_n(5))

# print("4.Reverse a string using Recursive Function ")
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("python"))

# print("5.palindrome using Recursive Function ")
# p=input("enter any word")
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]
# reversvalue = reverse_string(p)

# if p == reversvalue:
#     print("string is palindrome eg. mom",p)
# else:
#     print("string is not palindrome",p)

# print("6. Power of a number using Recursive Number")
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n-1)

# print(power(2, 5))

x = 62
y = 62
if x > y:
    print("x is greater")
elif y > x:
    print("y is greater")
else:
    print("both are equal")