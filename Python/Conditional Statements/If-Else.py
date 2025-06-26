#  If-Else Conditional Statement:
# The if-else statement extends the if statement by adding an else clause. If the condition is false, the program executes the code in the else block.

# Syntax of If-Else Conditional Statement:

# if(condition){
#     # Code execute if condition is true.
# } else{
#     # Code execute if condition is false.
# }

# Check whether the no is greate than 10, add +1 or if smaller than 10 then -1

num = int(input("Please Enter the number.: "))

if(num > 10) :
    print("Your updated number is: ", num + 1)
else : 
    print("Your uppdated number is: ", num - 1)

# Output
# Please Enter the number.: 34
# Your updated number is:  35

# Please Enter the number.: 2
# Your uppdated number is:  1