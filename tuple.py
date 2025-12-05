myTuple = (10,20,30,40,50,60)
print(type(myTuple) )

#tuple constructor
tuple2 = tuple(("aaa","bbb","ccc","aaa"))
print(type(tuple2))
print(tuple2)

print(myTuple)

#ordered, unchangable, allow duplicates, indexed

print(myTuple[1])

myTupple3 = ("kaveri",)
print(myTupple3)
print(type(myTupple3))


print(tuple2[1:3])
print(tuple2[-1])
print( tuple2[:3])

print("aaa" in tuple2)
print("ddd" not in tuple2)

changedTuple = list(tuple2)
print(changedTuple)

changedTuple[3] = "ddd"
print(changedTuple)

tuple2 = tuple(changedTuple)
print(tuple2,"after changes")


# unpacking
# (n1,n2,n3) = myTuple
# print(n1)

# (n1,n2,*n3) = myTuple
# print(n2)
# print(n3)


(n1,*n2,n3) = myTuple
print(n2)
print(n3)