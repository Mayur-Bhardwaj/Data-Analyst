# For Loop:- Python For Loops are used for iterating over a sequence like lists, tuples, strings, and ranges.
#  Iterable objects are those objects that allows are to iterate/move over every element of itself.
# Ex:- List(go in every element through indexing), tuple, dictionary(through key-value pair).
#  Types of Iteerable Objects:- List, Tuple, Sets, Dictionary, Range, String.

# Iterable Objects

list1 = ["Python","Django","Flask","FastAPI"]

# for l in list1:
#     # print(l)

# Output:-
# Python
# Django
# Flask
# FastAPI

list2 = ["Apple","Mango", "Orange", "Banana"]
for l2 in list2:
    print(l2)
    
# print(list2[1:4])

# Output:-
# Apple
# Mango
# Orange
# Banana
# ['Mango', 'Orange', 'Banana']

# For Loop

a = "Python Programming"

for i in a:
    print(i)

# Output:
# P
# y
# t
# h
# o
# n
 
# P
# r
# o
# g
# r
# a
# m
# m
# i
# n
# g

b = "Data Analyst"
for i in b:
    print(i, end="-")

# Output:
# D-a-t-a- -A-n-a-l-y-s-t-

fruits = ["Apple", "Mango", "Banana", "Orange", "Papaya"]

for j in fruits:
    print(j, end=",")   # Note:- "end" is used to make the data in one line

# Output:
# Apple,Mango,Banana,Orange,Papaya, 

# In the below list, number that is divisible by 2 multiply by 2 else multiply by 3.

list_data = [1,2,3,4,5,6,7,8,9,10,11,12]

for k in list_data:
    if(k%2==0):
        print(k*2)
    else:
        print(k*3)

# Output:-
# 3
# 4
# 9
# 8
# 15
# 12
# 21
# 16
# 27
# 20
# 33
# 24

#For Loop in Dictionary

dict = {
    "name"             : "John",
    "age"              :  28,
    "city"             : "New York",
    "country"          : "USA",
    "profession"       : "Data Analyst",
    "salary"           : 70000,
    "married"          : "False",
    "skills"           : {"Python", "SQL", "Excel", "Power BI"},
    "department"       : "Analytics",
    "experience_years" : 5
}
print(dict.keys())     # dict_keys(['name', 'age', 'city', 'country', 'profession', 'salary', 'married', 'skills', 'department', 'experience_years'])
print(dict.values())   # dict_values(['John', 28, 'New York', 'USA', 'Data Analyst', 70000, 'False', {'Python', 'Power BI', 'Excel', 'SQL'}, 'Analytics', 5])

# For iteration in Dictionary we need keys

for d in dict.keys():
    print(d)
    print(dict[d])
    print("*****")
 

# Output:
# name
# John
# *****
# age
# 28
# *****
# city
# New York
# *****
# country
# USA
# *****
# profession
# Data Analyst
# *****
# salary
# 70000
# *****
# married
# False
# *****
# skills
# {'Excel', 'Power BI', 'Python', 'SQL'}
# *****
# department
# Analytics
# *****
# experience_years
# 5
# *****

# For Loop in Sets

mySet = {10,20,30,40,50}

for m in mySet:
    print(m)

# Output:
# 50
# 20
# 40
# 10
# 30
