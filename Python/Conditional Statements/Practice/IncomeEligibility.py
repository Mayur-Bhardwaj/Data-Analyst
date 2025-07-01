# Write a program to check loan eligibility based on the user input. Takes the user's age, income and credit score as input.
# Apply the following conditions:
# If the age is 21 or older and the credit score is 700 or higher, display "Eligible for all Loans".
# If the credit score is below 700 but the income is greater than 50,000 display "Elegibile for small loans".
# Otherwise display "Not Eligible for Loans".

user_age = int(input("Please Enter your Age here: "))
user_income = float(input("Please Enter your Income here: "))
user_creditScore = int(input("Please Enter your Credit Score here: "))

if user_age >21 and user_creditScore == 700:
    print("Congratulations !! Eligible for All Loans.")
elif user_creditScore < 700 and user_income > 50000:
    print("Eligible For Small Loans.")
else:
    print("Oops !! Not Eligible For any Loans.")


# Output:
# Please Enter your Age here: 35
# Please Enter your Income here: 40000
# Please Enter your Credit Score here: 829
# Oops !! Not Eligible For any Loans.


# Please Enter your Age here: 25
# Please Enter your Income here: 80000
# Please Enter your Credit Score here: 578
# Eligible For Small Loans.

# Please Enter your Age here: 25
# Please Enter your Income here: 90000
# Please Enter your Credit Score here: 700
# Congratulations !! Eligible for All Loans.