a = [1,2,3,4,5]
print(a)        # [1, 2, 3, 4, 5]

a = [1,2,3,4,5,"Python","Data"]
print(a)        # [1, 2, 3, 4, 5, 'Python', 'Data']


# If we fetch the value from the list.

data = [1, 2, 3, 4, 5, 6, "DA", "SE"]
print(data[6])   #  DA

list_1 = ["Ram","Program", 'shyam', "Sati"]
print(list_1)     # ['Ram', 'Program', 'shyam', 'Sati']
print(list_1[2])  # shyam

# print(list_1[9])   # IndexError: list index out of range

# If we want multiple values then we use Slicing.

a = [1,2,3,4,5]  # display values from 2nd index to 5-1 = 4th index.
print(a[2:5])   # [3, 4, 5]
print(a[1:3])   # [2, 3]

print(a[2:])  # [3,4,5]
# Here [2:] means  display va;ues from starting 2nd index to last index all print

print(a[:4])  # [1, 2, 3, 4]
# Display from starting to the 4-1 = 3rd index

# Note:-  If we want the range of number that the value is print in between the index so we use slicing.
# String slicing in Python is a way to get specific parts of a string by using start, end and step values. It’s especially useful for text manipulation and data parsing.

b = [1,2,3,4,5,6,7,8,9,10]
print(b[2:7])  # [3, 4, 5, 6, 7]
print(b[:7])   # [1, 2, 3, 4, 5, 6, 7]
print(b[5:])   # [6, 7, 8, 9, 10]


b[4] = "Natraj"
print(id(b))    # 1650441598400
print(b)        # [1, 2, 3, 4, 'Natraj', 6, 7, 8, 9, 10]
print(id(b))    # 1650441598400

b[6] = "Apsara"
print(b)        # [1, 2, 3, 4, 'Natraj', 6, 'Apsara', 8, 9, 10]
print(id(b))    # 1650441598400

# If we want to insert the value at any index here suppose we want to insert value at index 3.
# By using the insert function we do it.

b.insert(2,"Radhika")
print(b)   # [1, 2, 'Radhika', 3, 4, 'Natraj', 6, 'Apsara', 8, 9, 10]
    