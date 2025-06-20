# Dictionary :  Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Suppose there is  a week: The week are the key and the Sunday, Monday, ..... are the values.

# Syntax:- { Key: Value, Key: Value, ..... }

var = {
    "roll": 1,
    "Name": "Akshay",
    "City": "Lucknow"
}
print(var)  # {'roll': 1, 'Name': 'Akshay', 'City': 'London'}

# Add Multiple values

dict = {
        "Roll": {1,2,3,4,5},
        "Name": ["Akshay","Ram", "Paras", "Nikhil", "Ansh"],
        "City": ["Lucknow", "Ayodhya", "Delhi", "Gurgaon", "Meerut"]
}
print(dict)  # {'Roll': {1, 2, 3, 4, 5}, 'Name': {'Akshay', 'Nikhil', 'Ram', 'Paras', 'Ansh'}, 'City': {'Lucknow', 'Ayodhya', 'Delhi', 'Gurgaon', 'Meerut'}}
print(id(dict))  # 1483437423936

# Note: Keys cannot be duplicate. If same name multiple keys then later one will override previous one.

dict_2 ={
    "roll": [1,2,3,4,5],
    "roll": ["a",'s','d',"f",'g']
}
print(dict_2)   # {'roll': ['a', 's', 'd', 'f', 'g']}

dict_3 ={
    "roll": [1,2,3,4,5],
    "roll": ["a",'s','d',"f",'g'],
    "roll": [2],
    "Roll": [90,78]   #Python is case-sensitive so 2 different values make.
}
print(dict_3)   #{'roll': [2], 'Roll': [90, 78]}

# Unordered Collection means there is no indexing. We acces using key value pair. We use keys to get values.

data = {
    "roll": [1,2,3,4,5],
    "Name": ["Anurag", "Bharat", "Chiraj", "Dharya","Eishwaran"],
    "City": ["Pune", "Banglore","Mumbai", "Noida", "Gurugram"]
}

print(data)   # {'roll': [1, 2, 3, 4, 5], 'Name': ['Anurag', 'Bharat', 'Chiraj', 'Dharya', 'Eishwaran'], 'City': ['Pune', 'Banglore', 'Mumbai', 'Noida', 'Gurugram']}
print(data["City"])    # ['Pune', 'Banglore', 'Mumbai', 'Noida', 'Gurugram']


data["City"].append("Kashmir")
print(data)    # {'roll': [1, 2, 3, 4, 5], 'Name': ['Anurag', 'Bharat', 'Chiraj', 'Dharya', 'Eishwaran'], 'City': ['Pune', 'Banglore', 'Mumbai', 'Noida', 'Gurugram', 'Kashmir']}


data["Name"].pop()
print(data)   # 'Name': ['Anurag', 'Bharat', 'Chiraj', 'Dharya'],


print(dict)   # {'Roll': {1, 2, 3, 4, 5}, 'Name': {'Ram', 'Nikhil', 'Paras', 'Ansh', 'Akshay'}, 'City': {'Gurgaon', 'Meerut', 'Lucknow', 'Ayodhya', 'Delhi'}}

dict["Roll"] = [11,22,33,44,55]

print(dict)    # {'Roll': [11, 22, 33, 44, 55], 'Name': {'Nikhil', 'Paras', 'Ansh', 'Ram', 'Akshay'}, 'City': {'Meerut', 'Gurgaon', 'Delhi', 'Lucknow', 'Ayodhya'}}
print(id(dict))  # 1483437423936


# If we add new key value pair then we use update

dict.update({"Admission": [2012, 2015, 2016, 2018, 2020]})
print(dict)    # {'Roll': [11, 22, 33, 44, 55], 'Name': {'Paras', 'Nikhil', 'Ram', 'Akshay', 'Ansh'}, 'City': {'Gurgaon', 'Lucknow', 'Ayodhya', 'Delhi', 'Meerut'}, 'Admission': [2012, 2015, 2016, 2018, 2020]}
print(id(dict))   # 1483437423936

# If we want to delete the key value pair so we use to delete like:

del dict["Admission"]

print(dict)  # {'Roll': [11, 22, 33, 44, 55], 'Name': {'Ansh', 'Paras', 'Akshay', 'Ram', 'Nikhil'}, 'City': {'Gurgaon', 'Ayodhya', 'Lucknow', 'Delhi', 'Meerut'}}

# If we want to delete wholw dictionary

del dict
print(dict)