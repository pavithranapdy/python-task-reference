# #2. check if a no. is positive, negative, or zero
# print("2. check if a no. is positive, negative, or zero")
# def numbers(x):
#   if x > 0:
#     print(x,"is +ve Value")
#   elif x < 0:
#     print(x,"is -ve Value")
#   else:
#     print(x,"is Zero Value")

# numbers(x = int(input("Enter the No.")))

# #3. find the largest of three nos.
# print("3. find the largest of three nos.")
# def largestNo(a,b,c):
#   if a>b and a>c:
#     print(a,"is largest value")
#   elif b>a and b>c:
#     print(b,"is largest value")
#   else:
#     print(c,"is largest value")

# a=int(input("enter any no."))
# b=int(input("enter any no."))
# c=int(input("enter any no."))
# largestNo(a,b,c)

# def. function related
def sum_of_evens(mylist):
    total = 0
    for num in mylist:
        if num % 2 == 0:
            total += num
    return total

mylist = [1, 2, 3, 4, 5, 6]
print("Sum of even numbers:", sum_of_evens(mylist))

