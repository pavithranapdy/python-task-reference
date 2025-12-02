mylist = [3, 4, 5, 6, 44, 55, 22]
print("My list= ", mylist)
# # #1. write a programm to print all elements of a list using a loop
# # print("1. write a programm to print all elements of a list using a loop")
# # for i in mylist:
# #     print("my list value is", i)

# # #2. write a python program to print only the even nos. from a list
# # print("2. write a python program to print only the even nos. from a list")
# # count =""
# # for i in mylist:
# #     if i % 2 == 0:
# #         s=str(i)
# #         count+=s
# #         #v=list(count)
# # print("even nos. in a list", count)

#3. write a python program to print only the odd nos. from a list
print("3. write a python program to print only the odd nos. from a list")
mylist = [3, 4, 5, 6, 44, 55, 22]
count =[]
for i in mylist:
    if i % 2 != 0:
        # s=str(i)
        count.append(i)
        #v=list(count)
print("odd nos. in a list",count)
  
# # #4. write a programm to find the sum of all nos. in a list
# # print("4. write a programm to find the sum of all nos. in a list")
# # count = 0
# # for i in mylist:
# #     count+=i
# # print("sum of all nos. in a list", count)

# # #5. write a python program to find the largest no. in a list using a loop
# # print("5. write a python program to find the largest no. in a list using a loop")
# # count =mylist[0]
# # for i in mylist:
# #     if i > count:
# #         count = i
# # print("largest no. in a list",count)

# # #6. write a python program to find the smallest no. in a list using a loop
# # print("6. write a python program to find the smallest no. in a list using a loop")
# # count =mylist[0]
# # for i in mylist:
# #     if i < count:
# #         count = i
# # print("smallest no. in a list",count)

# # #7. write a python program to how many positive nos. in a list
# # s=[2,4,7,-1,22,33,-3]
# # print("7. write a python program to how many positive nos. in a list")
# # print("my list is ", s)
# # j=0
# # for i in s:
# #     if i >= 0:
# #         j+=1
# # print("No. of +ve Nos. in a list", j)

# # #8. write a python program to how many negative nos. in a list
# # print("8. write a python program to how many negative nos. in a list")
# # j=0
# # for i in s:
# #     if i < 0:
# #         j+=1
# # print("No. of -ve Nos. in a list", j)

# # #9. write a python program to reverse a list without using the .reverse() method
# # print("9. write a python program to reverse a list without using the .reverse() method")
# # print("mylist: ", mylist)
# # print(mylist[::-1])

# #10. write a python program to count how many even & odd nos. in a list
# print("10. write a python program to count how many even & odd nos. in a list")
# even_nos =0
# for i in mylist:
#     if i % 2 == 0:
#         even_nos+=1
# print("even nos. in a list ",even_nos)
# odd_nos= len(mylist) - even_nos 
# print("odd nos. in a list ",odd_nos)

# # #11. write a python program to find and print the index of a specific value in a list
# # print("11. write a python program to find and print the index of a specific value in a list")
# # print("mylist", mylist)
# # specific_value = int(input("enter specifie value in my list"))
# # index=0
# # for i in mylist:
# #     index+=1
# #     if i == specific_value:
# #         print("index value of ", i,"is", index)

# # #12. write a python program to replace all -ve nos. in a list with 0
# # print("12. write a python program to replace all -ve nos. in a list with 0")
# # print(s)
# # count=""
# # for i in s:
# #     if i>0:
# #         positive_value=str(i)
# #         count+=positive_value
# #     if i < 0:
# #         i=0
# #         negative_value=str(i)
# #         count+=negative_value
# # print("Replace of all -ve Nos. in a list with 0 ", count)

# # #13. write a python program to print all Nos. greater than 50 in a list
# # print("13. write a python program to print all Nos. greater than 50 in a list")
# # print(mylist)
# # count=""
# # for i in mylist:
# #     if i >= 50:
# #         greaterthan_50 = str(i)
# #         count += greaterthan_50
# # print("print all Nos. greater than 50 in a list ", count)

# #14. write a program to create a new list containing the squares of each element
# s= [2, 3, 4, 5]
# print("My List ", s)
# count=""
# for i in s:
#   j=i**2
#   print("new list containing the squares of each element",j)

# # #15. write a python program to print all duplicate value in a list
# # print("15. write a python program to print all duplicate value in a list")
# # duplicate_value = [3,4,5,3,11,12,11]
# # result = ""
# # for ch in duplicate_value:
# #    if ch not in duplicate_value:
# #        result += str(ch)
# #        print(ch)

# # #16. write a program to print list elements until the no. 50 appears (stop when found)
# # mylist=[2,4,5,33,44,55,22]
# # print("My List ", mylist)
# # count=""
# # for i in mylist:
# #   if i < 50:
# #     s=str(i)
# #     count+=s
# #   else:
# #     break
# # print("print list elements until the no. 50 appears",count)

# #17. write a python program to count how many nos. in a list are divisible by 5
# print("17. write a python program to count how many nos. in a list are divisible by 5")
# j=0
# for i in mylist:
#     if i %5 ==0:
#         j+=1
# print("No. of Nos. in a list are divisible by 5 is ", j)

# #18. write a python program to find the second largest no. in a list using a loop
# print("18. write a python program to find the second largest no. in a list using a loop")
# max1 = max2 = 0
# for i in mylist:
#     if i > max1:
#         max2 = max1
#         max1 = i
#     elif i > max2 and i != max1:
#         max2 = i
# print("2nd largest no. in a list", max2)

# #19. To check whether the lis is assending order
# print("19. To check whether the lis is assending order")
# mylist1=[3,5,8,11,33,44]
# for i in range(len(mylist1)-1):
#   if mylist1[i] < mylist1[i+1]:
#     print("list is assending order")
#     break
#   else:
#     print("list is not assending order") 

# #20. write a python program to find the sum of  only the even nos. in a list
# print("20. write a python program to find the sum of  only the even nos. ")
# i_value =""
# count=0
# for i in mylist:
#     if i % 2 == 0:
#         count+=i
#         s=str(i)
#         i_value+=s
#         #v=list(count)
# print("even nos. in a list is", i_value ,"sum is ", count)

