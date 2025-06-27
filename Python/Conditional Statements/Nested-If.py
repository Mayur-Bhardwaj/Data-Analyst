# Write a program that suggests activities based on the user's age:
# If the Age is less than 18 , Suggest Yor are not eligible for Kids Activities.
# If ages is b/w 18  to 60 then check gender.
# If male suggessts "Ypu can participate in sports events".
# If female suggests "You can join yoga or dance classes".
# FOr age above 60, suggets "You can participate in senior citizen activities".


age = int(input("Please Enter Your age: "))
gender = (input("Please Enter Your Gender"))

if age<18:
    print("You are eligible for kids activities.")
elif age >= 18 and age <60:
    if (gender== "M" or gender == "m" or gender == "Male"):
        print("You can participate in Sports Events.")
    elif(gender == "F" or gender == "f" or "Female"):
        print("You can join yoga or dance classes")
    else:
        print("Invalid Gender, Please Enter Correct Gender either (M/F)")
else:
    print("You can participate in Senior Citizen Activities.")
    
      
# Output:

# Please Enter Your age: 56
# Please Enter Your Gender: m
# You can participate in Sports Events.

# Please Enter Your age: 10
# Please Enter Your Gender: Male
# You are eligible for kids activities.

# Please Enter Your age: 30
# Please Enter Your Gender: Female
# You can join yoga or dance classes


# Please Enter Your age: 60
# Please Enter Your Gender: Male
# You can participate in Senior Citizen Activities.