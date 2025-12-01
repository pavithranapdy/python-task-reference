#2. check if a no. is positive, negative, or zero
print("2. check if a no. is positive, negative, or zero")
x = int(input("Enter the No."))
match True:
    case _ if x > 0:
        print(x,"is +ve Value")
    case _ if x < 0:
        print(x,"is -ve Value")
    case _:
        print(x,"is Zero Value")

#3. find the largest of three nos.
print("3. find the largest of three nos.")
a=int(input("enter any no."))
b=int(input("enter any no."))
c=int(input("enter any no."))
match True:
    case _ if a>b and a>c:
        print(a,"is largest value")
    case _ if b>a and b>c:
        print(b,"is largest value")
    case _ :
        print(c,"is largest value")

#4. check if year is a leap year.
print("4. check if year is a leap year.")
year=int(input("enter year"))
match True:
    case _ if year%4 == 0:
        print(year,"is leap year")
    case _:
        print(year,"is not leap year")
        
#5. check if a no. is divisible by both 3 & 5.
print("5. check if a no. is divisible by both 3 & 5.")
a=int(input("enter any positive No."))
match True:
    case _ if a%3 == 0 and a%5 == 0:
        print(a,"is divisible by both 3 & 5")
    case _ if a%3 == 0 and a%5 != 0:
        print(a,"is divisible by  3")
    case _ if a%3 != 0 and a%5 == 0:
        print(a,"is divisible by  5")
    case _:
        print(a,"is not divisible by both 3 & 5")

#6. check if a no. is prime.
print("6. check if a no. is prime.")
a=int(input("enter any positive No."))
match True:
    case _ if a>=1 and a%2 != 0 and a%3 != 0 and a%4 != 0 and a%5 != 0:
        print(a,"is prime No.")
    case _:
        print(a,"is not prime No.")

#7. Check if a char. is vowel or consonant
print("7. Check if a char. is vowel or consonant")
char=(input("enter any letter"))
vowel=["a","e","i","o","u"]
match True:
    case _ if char in vowel:
        print(char,"is vowel")
    case _ if char not in vowel: 
        print(char,"is consonant") 
    case _:
        print("case is mismatch")
        
#8. check if a no. b/w 10 to 20
print("8. check if a no. b/w 10 to 20")
a=int(input("enter any positive No."))
match True:
    case _ if a>=10 and a<=20: 
        print(a,"is b/w 10 to 20")
    case _:
        print(a,"is not b/w 10 to 20")

        
