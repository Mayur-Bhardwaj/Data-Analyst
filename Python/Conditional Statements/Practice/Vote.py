#  Write a program that takes the user's age and nationality as input. 
#  If the user is at least 18 years old and their nationality is "Indian", print "Eligible to Vote".
#  If the user is younger than 18, calculate  and display then number of years left until they reach to voting age.
#  If the user's nationality is not "Indian" print "Not Eligible to vote in India". Ensure the program handles invalid inputs gracefully.

age = int(input("Please Enter your Correct Age here: "))
nationality = input("Please Enter your Nationality here: ")

if (age >= 18 and nationality == "Indian" or nationality == "indian"):
    print("Eligible for vote !!")
elif ( age < 18):
    print(f"You have {18-age} more years to become an eligible voter.")
else:
    print("Sorry !! You can't vote in India.")

# Output:
# Please Enter your Correct Age here: 25
# Please Enter your Nationality here: indian
# Eligible for vote !!

# Please Enter your Correct Age here: 12
# Please Enter your Nationality here: Indian
# You have 6 more years to become an eligible voter.



# Update Version

age_user = int(input("Please Enter your Correct Age here: "))

if( age_user >= 18):
    nationality_user = input("Please Enter your nationality here: ")
    if( age_user >= 18 and nationality_user == "Indian" or nationality_user == "indian"):
        print("Eligible for vote")
    else:
        print("Sorry, You are not eligible for vote...")    
else: 
    print(f"Sorry!! You are {18-age_user} more years to become an eligible voter.")



# Output:
# Please Enter your Correct Age here: 24
# Please Enter your nationality here: Indian
# Eligible for vote

# Please Enter your Correct Age here: 14
# Sorry!! You are 4 more years to become an eligible voter.