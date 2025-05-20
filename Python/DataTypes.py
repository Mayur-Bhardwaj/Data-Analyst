# 1. Take  input length and breadth form user and print the area of rectangle.

length = int(input("Enter the Length of Rectangle"))
breadth = int(input("Enter the Bredth of Rectangle"))

area = length*breadth
print(f"The Area of Rectangle is {area}")

# Output:-
# Enter the Length of Rectangle 22
# Enter the Bredth of Rectangle 45
# The Area of Rectangle is 990

# 2. An employee wants to count total experience in years he has by itself, 
# to help him find his experience in the number of months and days(assuming each month is of 30 days).

numbers = int(input("Enter the number of days"))

month = numbers//30  #They give the Quotient without decimal  & "/" give the proper answer with decimal
days = numbers%30    

print(f"Experience for the person for {numbers} days is {month} month and {days} days.")

# Output:-
# Enter the number of days 125
# Experience for the person for 125 days is 4 month and 5 days.


# Ex:- 34/5  ----> 6.4   ||||||||||  34//5 ----> 6