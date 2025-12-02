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
s=input("enter any characters ")
case=""
for i in s:
   if i is " ":
      case+=""
   else:
      case+=i
print("remove all spaces in str "case)

##print("6. To find the frequency of each character in a string")
##string_value = input("Enter the string: ")
##check = ""
##for i in string_value:
##    if i not in check:
##        count = 0
##        for j in string_value:
##            if j == i:
##                 count += 1
##                 check += i
##    print(i,":", count)

# # #7. Write a program to count how many digits are present in a string.
# s=input("enter the any character ")
# count=0
# for i in s:
#   count=count+1
# print("digits are present in a string ",count)

###8.Write a program to check if a string contains only alphabetic characters (without using isalpha())
##
##print("8. To check if a string contains only alphabetic characters (without using isalpha())")
##string_value = input("Enter the string : ")
##only_alphabet = True
##for i in string_value:
##        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
##                only_alphabet = False
##                break
##if only_alphabet:
##        print("Has only alphabet")
##else:
##        print("Not only alphabet")

###9. Write a program to convert all lowercase letters in a string to uppercase manually using ASCII values.
##
##print("9. To convert all lowercase letters in a string to uppercase manually using ASCII values.")
##string_value = input("Enter the string : ")
##result = ""
##for i in string_value:
##    if i >= "a" and i <= "z":
##        result += chr(ord(i) - 32)
##    else:
##        result += i
##print(result)

# # 10 Write a program to print all characters located at even indices of a string.
# s=input("enter any characters ")
# count=""
# for i in s:
#   print(i)
#   count=i+count
# print("without string slicing ",count)
###11.Write a program to count the number of words in a string without using split().
##print("11. To count the number of words in a string without using split()")          
##string_value = input("Enter the sentence: ")
##count = 1
##for ch in string_value:
##    if ch == " ":
##        count += 1
##print("No. of words:", count)

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
###13.Write a program to find the longest word in a sentence
##print("13. To find the longest word in a sentence")
##s = input("Enter the sentence: ")
##words = s.split()
##res = ""
##for word in words:
##    if len(word) > len(res):
##            res = word
##print("Longest word:", res)

###14.Write a program to check whether two strings are anagrams of each other using loops.
##print("14. To check whether two strings are anagrams of each other using loops.")
##s1 = input("Enter first string: ")
##s2 = input("Enter second string: ")
##
##if len(s1) != len(s2):
##    print("Not Anagrams")
##else:
##    for ch in s1:
##        if ch not in s2:
##            print("Not Anagrams")
##            break
##    else:
##        print("Anagrams")

###15.Write a program to count how many special characters are present in a string.
##print("15. To count how many special characters are present in a string")
##sting_value = input("Enter the string: ")
##count = 0
##for ch in sting_value:
##    if not ch.isalnum():
##        count += 1
##print("No. Special characters in str: ", count)

###16. Write a program to print each character of a string a given number of times
##print("16. To print each character of a string a given number of times")
##string_value = input("Enter the string: ")
##n = int(input("How many times: "))
##for i in string_value:
##    print(i * n)

###17. Write a program to remove duplicate characters from a string using loops
##print("17. To remove duplicate characters from a string using loops")
##string_value = input("Enter the string: ")
##result = ""
##for ch in string_value:
##    if ch not in result:
##        result += ch
##print(result)

###18. Write a program to count the number of consonants in a given string.
##print("18. To count the number of consonants in a given string.")
##string_value = input("Enter the string: ")
##count = 0
##for ch in string_value:
##    if ch.isalpha() and ch not in "aeiou" and ch not in "AEIOU":
##        count += 1
##print("Consonants:", count)

###19.Write a program to capitalize the first letter of a string manually (without using capitalize())
##
##print("19. To capitalize the first letter of a string manually (without using capitalize())")
##string_value = input("Enter the string: ")
##first = string_value[0].upper()
##print(first + string_value[1:])

# #20. Write a program to print characters of a string until a vowel is encountered.
# print("20. To print characters of a string until a vowel is encountered.")
# string_value = input("Enter the string: ")
# for i in string_value:
#     if i in "aeiouAEIOU":
#         break
#     print(i)