# Ask the user if their height is in feet(ft) or meters(m) and their weight is in Pounds(lbs) or Kilograms(kg)
# Convert the input as needed:
#   --> If weight is in pounds, convert it into kilograms(1 pound = 0.453592 kg).
#   --> If height is in feet, convert it to meters(1foot=0.3048 meters).
# Validate the inputs to ensure the weight and height values are within a logical range.
# Calculate BMI.
# Provide health advice based on the calculated BMI.
#   --> BMI<18.5 Suggest "UnderWeight -Consult a nutritionist"
#   --> 18.5<= BMI <25 Suggest "Normal Weight - Keep It up!"
#   --> BMI >=30 Suggest "Obese - Seek medical advice"

height_unit = input("Enter the unit of Height: ")
weight_unit = input("Enter the unit of Weight: ")

if height_unit not in ['ft', 'm'] or weight_unit not in ['kg', 'lbs']:
    print("Please Enter a Valid Data!!")
else:
    height= float(input("Please Enter the Height: "))
    weight= float(input("Please Enter the Weight: "))
    if(height <0 and weight <0):
        print("Enter a Valid Respone.")
    if(height_unit == 'ft'):
        height = height*0.3048
    if(weight_unit == 'lbs'):
        weight = weight*0.453592
    print(height)
    print(weight)
    bmi = (weight)/(height**2)
print(f"The BMI is: {bmi}")


# Output:-
# Enter the unit of Height: m
# Enter the unit of Weight: kg
# Please Enter the Height: 1.85
# Please Enter the Weight: 80
# 1.85
# 80.0
# The BMI is: 23.37472607742878

# Enter the unit of Height: ft
# Enter the unit of Weight: lbs
# Please Enter the Height: 5.7
# Please Enter the Weight: 198
# 1.7373600000000002
# 89.811216
# The BMI is: 29.754382377339695