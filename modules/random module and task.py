import random
# # random module is used to generate random nos. & make random choices
# # Returns a random float between 0.0 to 1.0
# print(random.random())


# # random int b/w a & b random.randomint(a,b) 

# print(random.randint(1, 20))
# dice = random.randint(1, 6)
# print("Dice Number:", dice)

# # Generates a random number from a given range

# print(random.randrange(1, 20, 2))

# # Selects a random element from a list, tuple, or string

# names = ["aaa", "bbb", "ccc","dddd"]
# print(random.choice(names))

# # Shuffles the elements of a list randomly

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)

# #unique random elements from a sequence 

# numbers = [10, 20, 30, 40, 50]
# print(random.sample(numbers, 3))

# #random floating-point number between two given values

# print(random.uniform(1.5, 10.5))

#random module OTP generate task
name="pavithran"
password="XXXX"
user_name=input("enter your name")
user_password=input("enter your password")
if user_name != " " and user_password != " ":
    if user_name == name:
        if user_password == password:
            print("Login successfully")
            otp = random. randint(1000, 9999)
            print("Your OTP is:", otp)
        else:
            print("Password is incorrect")
    else:
        print("User name is incorrect")
else:
    print("User name and password is empty")