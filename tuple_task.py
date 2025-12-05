# 1. Create a tuple that contains an integer, a string, and a float.
print("# 1. Create a tuple that contains an integer, a string, and a float.")
tuple_value =("pavi", 22, 1.4)
print("Tuple",tuple_value)
print(type(tuple) )

# 2. Access the second element of the tuple (5, 10, 15, 20).
print("# 2. Access the second element of the tuple (5, 10, 15, 20).")
tuple_value=(5, 10, 15, 20)
print(tuple, "second value in tuple",tuple_value[1])

# 3. Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.
print("3. Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.")
tuple_value=(1, 2, 3, 4, 5)
print(tuple, "last two elements in the tuple",tuple_value[3:5])

# 4. Concatenate the tuples (1, 2) and (3, 4).
tuple1= (1, 2)
tuple2= (3, 4)
print("4. concatenate the tuple1 & tuple2 is ",tuple1, tuple2, tuple1+tuple2)

# 5. Repeat the tuple (7, 8) three times.
tuple_value= (7, 8)
print("5.repeat the tuple", tuple, "is", tuple_value*3)

# 6. Check if 15 is present in the tuple (10, 20, 15, 25).
print("6. Check if 15 is present in the tuple (10, 20, 15, 25)")
tuple_value= (10, 20, 15, 25)
s=15 in tuple_value
if s is True:
  print("15 is present in the tuple", tuple_value)
else:
  print("15 is not present in the tuple", tuple_value)

# 7. Find the length of the tuple (3, 6, 9, 12).
tuple_value = (3, 6, 9, 12)
print("7. length of the tuple (3, 6, 9, 12) is", len(tuple_value))

# 8. Find the maximum and minimum values in the tuple (4, 1, 8, 3).
print("8. Find the maximum and minimum values in the tuple (4, 1, 8, 3).")
tuple_value= (4, 1, 8, 3)
print("Max Value in the tuple (4, 1, 8, 3) is", max(tuple_value))
print("Min Value in the tuple (4, 1, 8, 3) is", min(tuple_value))

# 9. Convert the list [1, 2, 3, 4] into a tuple.
a = [1, 2, 3, 4]
s=tuple(a)
print("9. Convert the list [1, 2, 3, 4] into a tuple is", s)

# 10. Convert the tuple (10, 20, 30) into a list.
a = (10, 20, 30)
s=list(a)
print("10. Convert the tuple (10, 20, 30) into a list is", s)

# 11. Find the index of the element 30 in the tuple (10, 20, 30, 40).
tuple_value= (10, 20, 30, 40)
print("11. the index of the element 30 in the tuple (10, 20, 30, 40) is", tuple_value.index(30))

# 12. Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).
tuple_value= (2, 3, 2, 4, 2)
print("12. how many times 2 appears in the tuple (2, 3, 2, 4, 2)", tuple_value.count(2))

# 13. Unpack the tuple (100, 200, 300) into three separate variables.
tuple_value= (100, 200, 300)
(n1,n2,n3) = tuple_value
print("13. Unpack the tuple (100, 200, 300) into three separate variables", n1, n2, n3)

# 14. Swap the values of two tuples (1, 2) and (3, 4).
n1= (1, 2) 
n2= (3, 4)
list_n1=list(n1)
list_n1[0],list_n1[-1] = list_n1[-1], list_n1[0],
swap_n1= tuple(list_n1)
list_n2=list(n2)
list_n2[0],list_n2[-1] = list_n2[-1], list_n2[0],
swap_n2= tuple(list_n2)
print("14. Swap the values of two tuples (1, 2) and (3, 4) is", swap_n1,"&", swap_n2)

# 15. Create a tuple that contains two other tuples (1, 2) and (3, 4).
n1= (1, 2) 
n2= (3, 4)
new_tuple=n1,n2
print("15. Create a tuple that contains two other tuples (1, 2) and (3, 4) is", new_tuple)

# 16. Access the number 4 from the nested tuple ((1, 2), (3, 4)).
n=((1, 2), (3, 4))
n1=n[0]
n2=n[1]
print("16. Access the number 4 from the nested tuple ((1, 2), (3, 4))", n2[1])

# 17. Find the sum of all numbers in the tuple (5, 10, 15).
mytuple=(5, 10, 15)
count = 0
for i in mytuple:
    count+=i
print("17. sum of all nos. in a tuple (5, 10, 15", count)

# 18. Sort the elements of the tuple (40, 10, 30, 20) in ascending order.
n=(40, 10, 30, 20)
print("18. Sort the elements of the tuple (40, 10, 30, 20) in ascending order", sorted(n))

# 19. Reverse the elements of the tuple (1, 2, 3, 4, 5).
n=(1, 2, 3, 4, 5)
print("19. Reverse the elements of the tuple (1, 2, 3, 4, 5) ", n[::-1] )

# 20. Check if all elements in the tuple (5, 5, 5, 5) are identical.
print("20. Check if all elements in the tuple (5, 5, 5, 5) are identical.")
my_tuple = (5, 5, 5, 5)
if len(set(my_tuple)) == 1:
    print("All elements in the tuple are identical.")
else:
    print("Elements in the tuple are not all identical.")