import re

text = "I love Python programming"
match = re.search("Python", text)   #Searches anywhere in the string.

if match:
    print("Found!")

text = "I like Java"
new_text = re.sub("Java", "Python", text)  #Replace Text
print(new_text)
result = re.findall("like", text)   #findall
print(result)

#Basic Regex Input Validation
user_input = input("Enter text: ")

if re.match(r"^[a-zA-Z]+$", user_input):
    print("Only letters allowed")
else:
    print("Invalid input")

#Validate Digits Only
number = input("Enter number: ")

if re.fullmatch(r"\d+", number):
    print("Valid number")
else:
    print("Invalid number")

#Email Validation
email = input("Enter email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")