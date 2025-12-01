####1. Write a program to print numbers from 1 to 10 using a for loop.
##print("1. Write a program to print numbers from 1 to 10 using a for loop.")
##for i in range(1,11):
##    print(i)
##
####2. Write a program to print even numbers from 1 to 20 using a for loop.
##print("2. Write a program to print even numbers from 1 to 20 using a for loop")
##for i in range(1,21):
##    if i%2 ==0:
##        print(i)
##
####3. Write a program to print odd numbers from 1 to 20 using a for loop.
##print("3. Write a program to print odd numbers from 1 to 20 using a for loop.")
##for i in range(1,21):
##    if i%2!=0:
##        print(i)
##
####4. Write a program to print numbers from 10 to 1 in reverse order.
##print("4. Write a program to print numbers from 10 to 1 in reverse order.")
##for i in range(1,11):
##    i=11-i
##    print(i)
##
####5.Write a program to print the square of each number from 1 to 10.
##print("5.Write a program to print the square of each number from 1 to 10.")
##for i in range(1,11):
##    i=i**2
##    print(i)
##
####6.Write a program to print the multiples of 5 up to 50.
##print("6.Write a program to print the multiples of 5 up to 50.")
##for i in range(1,11):
##    i=i*5
##    print(i)
####
####7.Write a program to find the sum of numbers from 1 to 10.
##print("7.Write a program to find the sum of numbers from 1 to 10.")
##Sum=0
##for i in range(1,11):
##    Sum=Sum+i
##    print("i is",i, "sum of i is", Sum)
##print("the sum of Nos. from 1 to 10 is",Sum)
##
####8.Write a program to find the sum of even numbers from 1 to 20.
##print("8.Write a program to find the sum of even numbers from 1 to 20.")
##Sum=0
##for i in range(1,21):
##    if i%2==0:
##        Sum=Sum+i
##        print("Even No. i is ",i, " sum of i is", Sum)
##print("the sum of even Nos. from 1 to 10 is",Sum)
##
####9.Write a program to find the sum of odd numbers from 1 to 20.
##print("9.Write a program to find the sum of odd numbers from 1 to 20.")
##Sum=0
##for i in range(1,21):
##    if i%2!=0:
##        Sum=Sum+i
##        print("ODD No. i is ",i, " sum of i is", Sum)
##print("the sum of ODD Nos. from 1 to 10 is",Sum)
##
####10.Write a program to print the multiplication table of 7.
##print("Write a program to print the multiplication table of 7.")
##j=7
##for i in range(1,11):
##    a=i*j
##    print(i,"*",j,"=",a)
##
####11.Write a program to print numbers divisible by 3 from 1 to 30.
##j=3
##for i in range (1,31):
##    if i%j ==0:
##        print(i,"/",j,"=",int(i/j))
####
####12.Write a program to find the factorial of 5 using a for loop..
##print("12.Write a program to find the factorial of 5 using a for loop.")
##j=1
##for i in range(1,6):
##        j=j*i
##        print("i value is ",i,"factorial of i is",j)
##print("the factorial of 5 i.e., range(1,6)is",j)
##
####13.Write a program to print numbers from 1 to n (take any fixed n like 15)
##n=int(input("enter any positive No."))
##for i in range(1,n+1):
##    print(i)
##    
####14. Write a program to count the digits of a number (example: 54321)
##print("14. Write a program to count the digits of a number (example: 54321)")
##s=input("enter the Nos.")
##count=0
##for i in s:
##   count=count+1 
##   print("i/p value is ",i,"digit: ", count)
##print("Number of digits: ", count)
##
##15. Write a program to reverse a number using a for loop (example: 1234 → 4321)
##print("15. Write a program to reverse a number using a for loop (example: 1234 → 4321)")
##num = 1234
##rev = 0
##for i in range(4):     
##    if num != 0:
##        digit = num % 10
##        rev = rev * 10 + digit
##        num //= 10
##print(rev)
##
##print("16. To print the digits of a number (example: 987 → 9, 8, 7)")
##num = "987"
##for ch in num:
##    if ch.isdigit():
##        print(ch)

####17. Write a program to find the sum of digits of a number (example: 564 → 15).
##print("17. Write a program to find the sum of digits of a number (example: 564 → 15).")
##s=input("enter the Nos.")
##count=0
##for i in s:
##    count = count+int(i)
##    print(i,"is digit value","sum is",count)
##print("total sum of digit value is",count)
##
####18. Write a program to calculate power of a number using loops (example: 2⁵).
##print("18. Write a program to calculate power of a number using loops (example: 2⁵)")
##s=input("enter the power value")
##count=2
##for i in s:
##    count = count**int(i)
##    print(i,"is power value of 2","value is",count)

print("19.Check number is prime or not")
num = int(input("Enter a number: "))
count = 0    

for i in range(2, num):
    if num % i == 0:
        count += 1     

if count == 0:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")


print("20.Print star pattern")
for i in range (1,5):
    print("*" * i)

print("reverse print if star")
for i in range (1,5):
    print(" "(5-i),"" * i)



