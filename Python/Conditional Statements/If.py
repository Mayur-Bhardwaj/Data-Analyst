#  If Conditional Statement:
# The if statement is the most basic form of conditional statement. It checks if a condition is true. If it is, the program executes a block of code.

# Syntax: 

# if(condition){
#     # Code to be execute if conditon true
# }

# Take numeric input from user and  if no. is grester than 10 add one to it.

no = int(input("Please Enter the number. "))

# if(no > 10):
#      {
#     print("The no is greater than 10")
# }

if(no > 10):
    print(no+1)

print("Outside")

# Output:- Please Enter the No. 2
# Outside

# Please Enter the No. 45
# 46
# Outside


no = int(input("Please Enter the No. "))
 
if (no > 10):
    print(no + 1)
    print(no -2)
    
print(no-2)
    
print("Outside")

# Output
# Please Enter the No. 34
# 35
# 32
# 32
# Outside