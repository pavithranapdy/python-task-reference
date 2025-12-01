
###nested_if
##name="pavithran"
##password="XXXX"
##user_name=input("enter your name")
##user_password=input("enter your password")
##if user_name != " " and user_password != " ":
##    if user_name == name:
##        if user_password == password:
##            print("Login successfully")
##        else:
##            print("Password is incorrect")
##    else:
##        print("User name is incorrect")
##else:
##    print("User name and password is empty")

#1) check if a no. is a valid 4 digit PIN
print("1) check if a no. is a valid 4 digit PIN")
PIN=int(input("enter your PIN"))
if PIN != " ":
    if PIN >=1000 and PIN <=9999:
        print("Your No. is valid for 4 digit PIN")
    else:
        print("Your 4 digit PIN is not valid")
else:
    print("Your PIN is empty")

#2) check if a no. is single-digit, double-digit or more,
print("2) check if a no. is single-digit, double-digit or more,")
num=int(input("enter your number"))
if num != " ":
    if num >=0 and num <=9:
        if num >=10 and num <=99:
            print(num, "is a double digit no.")
        else:
           print(num, "is a single digit no.")
    else:
        print(num, "is a more than double digit no.")
else:
    print("Your No. is empty")    

#3) compare three nos., and check if all are equal,
print("3) compare three nos., and check if all are equal,")
num1=int(input("enter any valid no."))
num2=int(input("enter any valid no."))
num3=int(input("enter any valid no."))
if num1 != " " and num2 != " " and num3 != " ":
    if num1 == num2 == num3:
        print("three nos. are equal value")
    elif num1 >= num2 and num1>= num3:
        print(num1,"is a greater value compare to other two nos.")
    elif num2>=num1 and num2>=num3:
        print(num2,"is a greater value compare to other two nos.")
    else:
        print(num3,"is a greater value compare to other two nos.")
else:
    print("three nos are empty")

# 4) check if a no. is divisible by 5, and also divisible by 10,
print("4) check if a no. is divisible by 5, and also divisible by 10,")
num1=int(input("enter any valid no."))
if num1 != " ":
    if num1 %5 == 0:
        if num1 % 10 == 0:
            print(num1, "is divisible by 5 & 10")
        else:
            print(num1, "is not divisible by 10")
            print("but", num1, "is divisible by 5")
    else:
        print(num1, "is not divisible by 5")
else:
    print("enter any valid No.")

# 5) check if a no. is a 3 digit no.
print("5) check if a no. is a 3 digit no.")
num1=int(input("enter any valid no."))
if num1 != " ":
    if num1 >=100 and num1<=999:
         print(num1, "is three digit +ve No.")
    else:
         print(num1, "is not three digit +ve No.")
else:
    print("three nos are empty")

