# Tuple:-  Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Ex:- mytuple = ("apple", "banana", "cherry")


tup = (1,2,3,4,5,6)
print(tup)       # (1, 2, 3, 4, 5, 6)
print(id(tup))   # 2811146840544

print(tup[1])  # 2

# tup[2] ="Add"
# print(tup[2])   # Error:- TypeError: 'tuple' object does not support item assignment

# Note:- In tuple we only do indexing and slicing.

print(tup[1:4])   # (2, 3, 4)
