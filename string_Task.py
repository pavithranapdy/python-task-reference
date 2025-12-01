# #1. Write a program to count the number of vowels in a given string.
# s=input("enter the any character ")
# count=0
# vowels=("a","e","i","o","u")
# for i in s:
#   if i in vowels: 
#       count=count+1
# print("vowel in string ",count)

# #2. Write a program to reverse a string using a loop (without using slicing).
# s=input("enter the any character ")           # input is pavi
# print("using str.slicing ",s[:: -1])

# count=""                #"" = empty String or count=0 zero value 
# for i in s:
#   count=i+count         # i is 0 count=p+ "";count=p, i=1 count=a+p; count=ap
# print("without string slicing ",count)  # o/p id ivap

# #3. Write a program to check if a string is a palindrome using a loop
# stringvalue=input("enter the any string ")   # i/p is pavi
# reverse_stringvalue=stringvalue[::-1] #.replace(" ","")
# if stringvalue == reverse_stringvalue:
#   print("input string is Palindrome", stringvalue)
# else:
#   print("input string is not palindrome", stringvalue) 

# # 4. Write a program to count the no. of upper & lower letters in a str.
# s=input("enter any characters ")
# uppercase=0
# lowercase=0
# space=0
# for i in s:
#    if i.isupper():
#       uppercase+=1
#    elif i.islower():
#       lowercase+=1
#    else:
#       space+=1
      
# print("uppercase in str ",uppercase)
# print("lowercase in str ", lowercase)
# print("space in str ", space)

# 5. Write a program to remove all spaces from a string without using built-in replace().
# s=input("enter any characters ")
# case=""
# for i in s:
#    if i is " ":
#       case+=""
#    else:
#       case+=i
# print("remove all spaces in str "case)

# # #7. Write a program to count how many digits are present in a string.
# s=input("enter the any character ")
# count=0
# for i in s:
#   count=count+1
# print("digits are present in a string ",count)

# 10 Write a program to print all characters located at even indices of a string.
s=input("enter any characters ")
count=""
for i in s:
  print(i)
  count=i+count
print("without string slicing ",count)

# #12. Write a program to replace all vowels in a string with * using a loop.
# s=input("enter the any character ")
# count=""
# vowels=("a","e","i","o","u")
# for i in s:
#   if i not in vowels:
#      count=count+i
#   else: 
#       count=count+"*"
# print("vowel in string ",count)