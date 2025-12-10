#1. Create a set from a list of integers
print("1. Create a set from a list of integers")
mylist = [3, 4, 5, 6, 44, 55, 22]
print("My list= ", mylist)
s=set(mylist)
print("convert a list into set= ", s)

#2. check if an element exists in a set
print("2. check if an element exists in a set")
s={"aaa", "bbb", 12, 33}
print("my set", s)
specific_value = (input("enter specifie element in my set"))
index=0
for i in s:
    if i == specific_value:
        s=True
if s==True:
    print("specific element is present in my set ", specific_value)
else:
    print("specific element is not present in my set ", specific_value)

#3. Add an element to the set
print("3. Add an element to the set")
s={"aaa", "bbb", 12, 33}
print("my set", s)
s.add(22)
print("add an element 22 in my set", s)

#4. Remove an element to the set
print("4. Remove an element to the set")
print("my set", s)
s.remove(22)
print("remove an element 22 in my set", s)

#5. Use discard() to remove an element without throwing an error if it does not exist
print("5. Use discard() to remove an element without throwing an error if it does not exist")
print("my set", s)
s.discard(22)
print("Use discard() to remove an element 22 in my set", s)

#6. Find the Union of two sets
print("6. Find the Union of two sets")
set1={1,2,3,4}
set2={1,2,5,6,7}
print(set1, "&", set2, "the Union of two sets ", set1.union(set2))

#7. Find the Intersection of two sets
print("7. Find the intersection of two sets")
set1={1,2,3,4}
set2={1,2,5,6,7}
print(set1, "&", set2, "the Intersection of two sets ", set1.intersection(set2))

#8. Find the Difference of two sets
print("8. Find the Difference of two sets")
set1={1,2,3,4}
set2={1,2,5,6,7}
print(set1, "&", set2, "the Difference of two sets ", set1.difference(set2))

#9. Find the Symmetric of two sets
print("9. Find the Symmetric of two sets")
set1={1,2,3,4}
set2={1,2,5,6,7}
print(set1, "&", set2, "the Symmetric of two sets ", set1.symmetric_difference(set2))

#10. Find the Subset relationship b/w two sets
print("10. Find the Subset relationship b/w two sets")
set1={1,2}
set2={1,2,5,6,7}
subset= set1.issubset(set2)
if subset== True:
    print(set1, "&", set2, "are subset")
else:
    print(set1, "&", set2, "are not subset")

#11. Find the Superset relationship b/w two sets
print("11. Find the Superset relationship b/w two sets")
set1={1,2}
set2={1,2,5,6,7}
superset= set1.issuperset(set2)
if superset== True:
    print(set1, "&", set2, "are superset")
else:
    print(set1, "&", set2, "are not superset")

#12. Remove all elements from a set
print("12. Remove all elements from a set")
print("my set", s)
s.clear()
print("Remove all elements ", s)

#13. Iterate through a set
print("13. Iterate through a set")
s={"Iterate", "through", "a", "set"}
print("my set", s)
for i in s:
    print(i)

#14. Convert a set into a list
print("14. Convert a set into a list")
s={"Iterate", "through", "a", "set"}
print("my set", s)
convert_set=list(s)
print(convert_set)    

#15. Check if two sets are disjoint(no common elements)
print("15. Check if two sets are disjoint(no common elements)")
set1={1,2}
set2={1,2,5,6,7}
superset= set1.isdisjoint(set2)
if superset== True:
    print(set1, "&", set2, "are disjoint")
else:
    print(set1, "&", set2, "are not disjoint")

#16. Create a set from a string (unique characters)
print("16. Create a set from a string (unique characters)")
string= ("apple", "banana", "apple")
convert_string=set(string)
print(string, "Create a set from a string", convert_string)

#17. Find the length of a set
print("17. Find the length of a set")
s={"Iterate", "through", "a", "set"}
print("my set", s ,"length of my set is", len(s))

#18. use set comprehension to create a set of squares of numbers from 1 to 5
print("18. use set comprehension to create a set of squares of numbers from 1 to 5")
s={1,2,3,4,5}
print("my set", s)
count=[]
for i in s:
    i=i**2
    count.append(i)
print(set(count))
#19. check if a set is empty
print("19. check if a set is empty")
s={"Iterate", "through", "a", "set"}
print("my set", s)
empty_set={}
if s == empty_set:
    print("set is empty")
else:
    print("set is not empty")

#20. Find the unique elements from two lists using set
print("20. Find the unique elements from two lists using set")
list1=[1,2,3,4]
list2=[1,2,5,6,7]
set_1=set(list1)
set_2=set(list2)
print(list1, "&", list2, "unique elements from two lists using set ", set_1.intersection(set_2))


          
