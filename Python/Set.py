# SETS :-
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# We cannot access individual elements/variables of sets.
# Once created, edited is difficult.

sets = {1,2,3,4,5}
print(type(sets)) # <class 'set'>

# In sets we cannot add duplicate values. They store only unique values.

set1 = { 1,2,3,4,2,1,1,4,3}
print(set1)  # {1, 2, 3, 4}

sets.pop()
print(sets)  # {2, 3, 4, 5}
sets.pop()
print(sets)  # {3, 4, 5}

# Add new value

data = {1,2,3,4,5}
data.add(34)
print(data)  # {1, 2, 3, 4, 5, 34}

data2 = {21,23,45,79,90}
data2.add(34)
print(data2)  #{34, 21, 23, 90, 45, 79}   the result come in unorder because set store value in unordered manner


a = {34,21,76,87}
print(a)

# Remove element in Sets

a.remove(76)
print(a)  # {34, 21, 87}

string_set ={"Apple","Meta","Google","Amazon"}
print(string_set)  # {'Meta', 'Apple', 'Google', 'Amazon'}

# Set Theory

sets1= {1,2,3,4,5}
sets2 = {4,5,6,7,8}
print(f"Union = {sets1.union(sets2)}")  # Union = {1, 2, 3, 4, 5, 6, 7, 8}

print(f"Intersection = {sets1.intersection(sets2)}")   # Intersection = {4, 5}

print(f"A-B = { sets1-sets2 }")  # A-B = {1, 2, 3}
print(f"B-A = { sets2 - sets1 }")  # B-A = {8, 6, 7}


# Suppose we haave 2 list of students and we want only defaulters students 

student1 = {"Aman", "Aashish", "Priya", "Rohan", "Kajal"}
student2 = {"Aashish", "Priya", "Kajal"}
print(f"The defaulters students = {student1 - student2}") # The defaulters students = {'Rohan', 'Aman'}

# Note:- The f before the string is used to create an f-string, which stands for formatted string literal. It's a feature in Python (introduced in Python 3.6) that allows you to embed expressions inside string literals, using curly braces {}.

