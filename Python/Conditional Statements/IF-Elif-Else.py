# If-Elif-Else or If-Else-If Condition

# This condition is used when we have multiple conditions to check.
#  If the if condition is false, the program checks the next else if condition, and so on.

# Syntax:
# if(condition 1){
#     # Code execute if condition 1 is true
# } else if(condition 2) {
#     # Code execute if condition 2 is true
# } else {
#     # Code to be execute if all above conditon is false.
# }
    
# Take a numeric input from user, If number is greater than 10, add ine to it, If number is smaller than 10
# then subtract 1 from it, else print the number as it is.

number = int(input("Please Enter the number: "))

if( number > 10):
    print("Your updated number is : ", number + 1)
elif ( number < 10):
    print("Your updated number is: ", number - 1)
else: 
    print("Your updated number is: ", number)

# Output:
# Please Enter the number: 14
# Your updated number is :  15

# Please Enter the number: 5
# Your updated number is:  4

# Please Enter the number: 10
# Your number is:  10


# If user enter the value in decimal.

number = float(input("Please Enter the number: "))

if( number > 10):
    print("Your updated number is : ", number + 1)
elif ( number < 10):
    print("Your updated number is: ", number - 1)
else: 
    print("Your updated number is: ", number)

# Output
# Please Enter the number: 10.5
# Your updated number is :  11.5

