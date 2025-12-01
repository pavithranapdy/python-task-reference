#2. check if a no. is positive, negative, or zero
print("2. check if a no. is positive, negative, or zero")
x = int(input("Enter the No."))
if x > 0:
    print(x,"is +ve Value")
elif x < 0:
    print(x,"is -ve Value")
else:
    print(x,"is Zero Value")

#3. find the largest of three nos.
print("3. find the largest of three nos.")
a=int(input("enter any no."))
b=int(input("enter any no."))
c=int(input("enter any no."))
if a>b and a>c:
    print(a,"is largest value")
elif b>a and b>c:
    print(b,"is largest value")
else:
    print(c,"is largest value")

#4. check if year is a leap year.
print("4. check if year is a leap year.")
year=int(input("enter year"))
if year%4 == 0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#5. check if a no. is divisible by both 3 & 5.
print("5. check if a no. is divisible by both 3 & 5.")
a=int(input("enter any positive No."))
if a%3 == 0 and a%5 == 0:
    print(a,"is divisible by both 3 & 5")
else:
    print(a,"is not divisible by both 3 & 5")

#6. check if a no. is prime.
print("6. check if a no. is prime.")
a=int(input("enter any positive No."))
if a>=1 and a%2 != 0 and a%3 != 0 and a%4 != 0 and a%5 != 0:
    print(a,"is prime No.")
else:
    print(a,"is not prime No.")

#8. check if a no. b/w 10 to 20
print("8. check if a no. b/w 10 to 20")
a=int(input("enter any positive No."))
if a>=10 and a<=20: # AND both condition is true o/p is execute
    print(a,"is b/w 10 to 20")
else:
    print(a,"is not b/w 10 to 20")

#9. check if a no. is multiple of another no.
print("9. check if a no. is multiple of another no.")
a=int(input("enter any positive No."))
b=int(input("enter any positive No."))
if a%b == 0 or b%a == 0:# OR single condition is true o/p is execute
    print(a,"&", b, "is multiple of another no. ")
else:
    print(a,"&", b, "is not multiple of another no. ")

#10. find the smallest of three nos.
print("10. find the smallest of three nos.")
a=int(input("enter any no."))
b=int(input("enter any no."))
c=int(input("enter any no."))
if a<b and a<c:
    print(a,"is Smallest no.")
elif b<a and b<c:
    print(b,"is Smallest no.")
else:
    print(c,"is Smallest no.")

#11. check if a no. is perfect square
print("11. check if a no. is perfect square")
a=int(input("enter any positive No."))
b=a**0.5
if b**2 == a: 
    print(a,"is a perfect square")
else:
    print(a,"is not perfect square")
    
#13. check if a no. is multiple of  7
print("13. check if a no. is multiple of  7")
a=int(input("enter any positive No."))
if a%7 ==0: 
    print(a,"is multiple of 7")
else:
    print(a,"is not multiple of 7")

#14. check if two Nos. are equal
print("14. check if two Nos. are equal")
a=int(input("enter any positive No."))
b=int(input("enter any positive No."))
if a == b: 
    print(a,"&", b,"are equal No.")
else:
    print(a,"&", b,"are not equal No.")

#16. check if a no. is a multiple of 2, 3, or both
print("16. check if a no. is a multiple of 2, 3, or both")
a=int(input("enter any positive No."))
if a % 2 == 0 and a % 3 ==0: 
    print(a,"is multiple of 2 & 3")
elif a % 3 ==0:
    print(a,"is multiple of 3")
elif a % 2 == 0:
    print(a,"is multiple of 2")
else:
        print(a,"is not multiple of 2 & 3")

#17. check if a no. is divisible by 4 and not divisible by 6
print("17. check if a no. is divisible by 4 and not divisible by 6")
a=int(input("enter any positive No."))
if a % 4 == 0 and a % 6 !=0: 
    print(a,"is divisible by 4 and not divisible by 6")
elif a % 4 ==0 and a % 6 ==0:
    print(a,"divisible by 4 & 6")
elif a % 6 != 0 and a % 4 !=0:
    print(a,"is not divisible by 4 & 6")
elif a%4!=0 and a%6==0:
        print(a,"is not divisible by 4 and divisible by 6")

#19. check if a no. is divisible by 2 or 3
print("19. check if a no. is divisible by 2 or 3")
a=int(input("enter any positive No."))
if a % 2 == 0 and a%3==0: 
    print(a,"is divisible by 2 & 3")
elif a % 2 == 0 : 
    print(a,"is divisible by 2")
elif a % 3 ==0:
    print(a,"is divisible by 3")
elif a % 2 != 0 and a % 3 !=0:
    print(a,"is not divisible by 2 & 3")

#20. check if a no. is greater than 100 & divisible by 5
print("20. check if a no. is greater than 100 & divisible by 5")
a=int(input("enter any positive No."))
if a >100 and a%5==0: 
    print(a,"is greater than 100 & divisible by 5")
elif a <100 and a%5==0: 
    print(a,"is smaller than 100 & divisible by 5")
elif a % 5 !=0 and a<100:
    print(a,"is smaller than 100 & not divisible by 5")

#21. check if a no. b/w 50 to 150
print("21. check if a no. b/w 50 to 150")
a=int(input("enter any positive No."))
if a>50 and a<150: # AND both condition is true o/p is execute
    print(a,"is b/w 50 to 150")
else:
    print(a,"is not b/w 50 to 150")


#22. check if a no. is divisible by 2 but not 4
print("22. check if a no. is divisible by 2 but not 4")
a=int(input("enter any positive No."))
if a % 2 == 0 and a % 4 !=0: 
    print(a,"is divisible by 2 but not 4")
elif a % 2 ==0 and a % 4 ==0:
    print(a,"divisible by 2 & 4")
elif a % 2 != 0 and a % 4 !=0:
    print(a,"is not divisible by 2 & 4")
elif a%2!=0 and a%4==0:
        print(a,"is not divisible by 2 and divisible by 4")

#25. check if a no. greater than or equal to 0 but less than 100
print("25. check if a no. greater than or equal to 0 but less than 100")
a=int(input("enter any positive No."))
if a>=0 and a<100: # AND both condition is true o/p is execute
    print(a,"is greater than or equal to 0 but less than 100")
else:
    print(a,"is not greater than or equal to 0 but less than 100")
