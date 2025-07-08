# Enter 2 number, If 2nd number is greater, then swap the number then divide.

first_number = int(input("Please Enter your First Number here: "))
second_number = int(input("Please Enter your Second Number here: "))

if first_number >= second_number:
    print(f"{first_number} is greater than {second_number}")
else:
    first_number = first_number + second_number
    second_number = first_number - second_number
    first_number = first_number - second_number
    print(f"The first number after swap is {first_number}")
    print(f"The second number after swap is {second_number}")
    new_number = first_number/second_number
    print(f"The updated number is: {new_number}")
    

# Output:
# Please Enter your First Number here: 34
# Please Enter your Second Number here: 22
# 34 is greater than 22

# Please Enter your First Number here: 45
# Please Enter your Second Number here: 62
# The first number after swap is 62
# The second number after swap is 45
# The updated number is: 1.3777777777777778



# Updated Version

first_number = int(input("Please Enter your First Number here: "))
second_number = int(input("Please Enter your Second Number here: "))

if first_number >= second_number:
    print(f"{first_number} is greater than {second_number}")
        
# If second number is greater, swap the values
if second_number > first_number:
    # Swapping without a third variable
    first_number = first_number + second_number
    second_number = first_number - second_number
    first_number = first_number - second_number

# Now first_number is guaranteed to be greater than or equal to second_number
print(f"After swapping (if needed): First = {first_number}, Second = {second_number}")

# Avoid divide-by-zero error
if second_number != 0:
    result = first_number / second_number
    print(f"The result of division is: {result}")
else:
    print("Division by zero is not allowed.")



# Using 3rd Variable.

first_number = int(input("Please Enter your First Number here: "))
second_number = int(input("Please Enter your Second Number here: "))

if first_number >= second_number:
    print(f"{first_number} is greater than {second_number}")
else:
    temp = first_number
    first_number = second_number
    second_number = temp

    # first_number = first_number + second_number
    # second_number = first_number - second_number
    # first_number = first_number - second_number
    print(f"The first number after swap is {first_number}")
    print(f"The second number after swap is {second_number}")
    new_number = first_number/second_number
    print(f"The updated number is: {new_number}")
    

# Output:
# Please Enter your First Number here: 25
# Please Enter your Second Number here: 30
# The first number after swap is 30
# The second number after swap is 25
# The updated number is: 1.2


# Please Enter your First Number here: 15
# Please Enter your Second Number here: 12
# 15 is greater than 12
