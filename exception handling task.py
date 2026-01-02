#1. check if a no. is positive, negative, or zero
print("1. check if a no. is positive, negative, or zero")
def numbers(x):
  if x > 0:
    print(x,"is +ve Value")
  elif x < 0:
    print(x,"is -ve Value")
  else:
    print(x,"is Zero Value")
try:
  x = int(input("Enter the No."))
  numbers(x)
except ValueError:            
   print('please enter the valid No')
finally:
    print("Completed Question 1\n")

#2. find the largest of three nos.
print("2. find the largest of three nos.")
def value(a,b,c):
  if a>b and a>c:
    print(a,"is largest value")
  elif b>a and b>c:
    print(b,"is largest value")
  else:
    print(c,"is largest value")   
try:
  a=int(input("enter any no."))
  b=int(input("enter any no."))
  c=int(input("enter any no."))
  value(a,b,c)
except ValueError:            
    print("Please enter valid integer values (no letters or decimals")
finally:
    print("Completed Question 2\n")

#3. check if year is a leap year.
print("3. check if year is a leap year.")
def exmp3(year):
  if year%4 == 0:
    print(year,"is leap year")
  else:
    print(year,"is not leap year")
try:
   year=int(input("enter year"))
   exmp3(year)
except ValueError:            
    print("Please enter valid integer values (no letters or decimals")
finally:
    print("Completed Question 3\n")

#4. check if a no. is divisible by both 3 & 5.
print("4. check if a no. is divisible by both 3 & 5.")
def exmp4(a):
  if a%3 == 0 and a%5 == 0:
    print(a,"is divisible by both 3 & 5")
  else:
    print(a,"is not divisible by both 3 & 5")
try:
   a=int(input("enter any positive No."))
   exmp4(a)
except ValueError:            
    print("Please enter valid integer values (no letters or decimals")
finally:
    print("Completed Question 4\n")

#5. check if a no. is prime.
print("5. check if a no. is prime.")
def exmp5(a):
  if a>=1 and a%2 != 0 and a%3 != 0 and a%4 != 0 and a%5 != 0:
    print(a,"is prime No.")
  else:
    print(a,"is not prime No.")
try:
   a=int(input("enter any positive No."))
   exmp5(a)
except ValueError:            
    print("Please enter valid integer values (no letters or decimals")
finally:
    print("Completed Question 5\n")


