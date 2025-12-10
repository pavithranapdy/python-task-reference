# # 1. Given two lists, return the set of common elements that appear more than once in both lists.
# print("1. Given two lists, return the set of common elements that appear more than once in both lists")
# list1=[1,2,3,4]
# list2=[1,2,5,6,7]
# set_1=set(list1)
# set_2=set(list2)
# print(list1, "&", list2, "common elements from two lists using set ", set_1.intersection(set_2))

# # 2. Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.
# print("2. Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.")
# import string
# sentence = "Hello, world! How are you today?"
# # Remove punctuation
# clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))
# # Split into words and convert to a set
# unique_words = set(clean_sentence.split())
# print("My sentence is", sentence, "set of unique words from a sentence", unique_words)

# 3. Write a function that takes a list of numbers and returns the largest subset such that the sum of the subset is even.



# 4. Given a set of integers, write a function that returns a new set containing all subsets of the original set.


# # 5. Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality).
# print("5. Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality)")
# set1={1,2,5,6,7}
# set2={1,5,6,7,2}
# if set1==set2:
#   print(set1, "&", set2, "are equal")
# else:
#   print(set1, "&", set2, "are not equal")

# # 6. Write a program that finds the intersection of multiple sets.
# print("6. Write a program that finds the intersection of multiple sets")
# set1={1,2,5,6,7}
# set2={1,2,3,4}
# set3={1,2,5,6,8}
# print("the multiple sets ", set1, set2, "&", set3)
# intersection=set1.intersection(set2,set3)
# print("intersection of multiple sets is ", intersection)

# # 7. Find the set difference of multiple sets.
# print("7. Find the set difference of multiple sets")
# set1={1,2,5,6,7}
# set2={1,2,3,4}
# set3={1,2,5,6,8}
# print("the multiple sets ", set1, set2, "&", set3)
# difference=set1.difference(set2, set3)
# print("intersection of multiple sets is ", difference)

# 8. Given a list of sets, write a program to return the set containing elements that are present in every set in the list.
sets = [{1, 2, 3}, {2, 3, 4}, {2, 5, 3}, {3}]

def intersection_of_sets(list_of_sets):
    if not list_of_sets:
        return set()  # no sets → return empty set
    
    result = list_of_sets[0].copy()
    
    for s in list_of_sets[1:]:
        result &= s   # intersection
    
    return result
print(intersection_of_sets(sets))

# 9. Write a function that checks if a set of strings forms a palindrome when concatenated together.

def can_form_palindrome(strings):
    from collections import Counter
    
    char_count = Counter()
    
    # Count all characters across all strings
    for s in strings:
        char_count.update(s)
    
    # Count how many characters have odd frequency
    odd_counts = sum(1 for c in char_count.values() if c % 2 != 0)
    
    # A palindrome can have at most one odd-count character
    return odd_counts <= 1
print(can_form_palindrome({"abc", "bac"}))


# 10. Given a set, find the number of distinct subsets where the sum of the elements in each subset is divisible by a given integer.
# 11. Write a program that finds the longest consecutive sequence in an unsorted list of numbers using sets.
# 12. Given two sets, find the symmetric difference, but only include elements that appear more than once across both sets.
# 13. Write a function that checks if there exists a pair of numbers in a set that sum to a specific target.
# 14. Write a function to determine whether a set is a proper subset of another set.
# 15. Write a function that returns the elements in a set which are not present in any of the other sets from a list of sets.
# 16. Find all possible subsets of a set and return the ones where the sum of elements is prime.
# 17. Create a set of all permutations of a given list of characters.
# Write a program that finds the longest consecutive sequence in an unsorted list of numbers using sets.
# 19. Find the number of elements that appear in exactly one set from a list of sets.
# 20. Write a function that finds the union of all sets, but only includes elements that appear more than once across all sets.