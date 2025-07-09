# Print the Odd number till n(asked from user).

number = int(input("Please Enter the term till which you want to print the odd number: "))

for i in range(1, number+1, 2):
    print(i)


#Output:
# Please Enter the term till which you want to print the odd number: 10
# 1
# 3
# 5
# 7
# 9 

# Please Enter the term till which you want to print the odd number: 25
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25

# Add the Odd number inside the list

number = int(input("Please Enter the term till which you want to print the odd number: "))
list = []
for i in range(1, number+1, 2):
   list.append(i)
   print(list)


# Output:
# Please Enter the term till which you want to print the odd number: 20
# [1]
# [1, 3]
# [1, 3, 5]
# [1, 3, 5, 7]
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9, 11]
# [1, 3, 5, 7, 9, 11, 13]
# [1, 3, 5, 7, 9, 11, 13, 15]
# [1, 3, 5, 7, 9, 11, 13, 15, 17]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]