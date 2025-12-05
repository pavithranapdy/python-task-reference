# unordered, not allow duplicated, unindexed

mySet = {10,20,30,40,50,10}
print(type(mySet))
print(mySet)

#add()

mySet.add(60)
print(mySet)

# update - Adds multiple elements (from any iterable).
myList = [1,2,3]
mySet.update(myList)
print(mySet)

# remove -Removes the element; raises KeyError if not found.

mySet.remove(20)
print(mySet)


# discard - Removes the element; not raises KeyError if not found.
mySet.discard(20)
print(mySet)

# pop() - used to remove random element bcoz set are unordered

mySet.pop()
print(mySet)

# clear()
# mySet.clear()
# print(mySet)



#union() - Returns all elements from both sets.
set1 = {1,2,3}
set2 = {1,4,2}

print(set1.union(set2))

# intersection() - returns the commom data from both sets
print(set1.intersection(set2))

# difference() - Elements in the first set but not in the second.
print(set1.difference(set2))

# symmetric_difference() - Elements in either set but not both.
print(set1.symmetric_difference(set2))


# Relationship Test Methods

# issubset() - Checks subset

print({1, 2}.issubset({1, 2, 3})  )

# issuperset()

print({10,20,30,40}.issuperset({20,30,10,78}))

# isdisjoint() Returns True if no elements are common.

print({"a","b","c"}.isdisjoint({"d","e","f"}))