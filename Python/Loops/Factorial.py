# Write a program to find the Factorial of a number.

number = int(input("Please Enter the number to calculate Factorial: "))

fact = 1
i =1
while i<=number:
   fact = fact*i
   i = i+1

print(f"The Factorial of {number} is {fact}")



# Output:
# Please Enter the number to calculate Factorial: 5
# The Factorial of 5 is 120

# Please Enter the number to calculate Factorial: 12
# The Factorial of 12 is 479001600