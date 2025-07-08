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
    
if(bmi<= 18.5):
    print("UnderWeight - Consult A Nutritionist")
elif ( bmi >= 18.5 and bmi < 25):
    print("Normal Weight - Keep It Up!!")
elif (bmi >= 25 and bmi < 30):
    print("OverWeight - Consider regular exercise")
elif (bmi >= 30):
    print("Obese - Seek Medical Advice")


# Output:-
# Enter the unit of Height: ft
# Enter the unit of Weight: kg
# Please Enter the Height: 6.2
# Please Enter the Weight: 92
# 1.88976
# 92.0
# The BMI is: 25.76170026892025
# OverWeight - Consider regular exercise

# Enter the unit of Height: m
# Enter the unit of Weight: lbs
# Please Enter the Height: 1.8
# Please Enter the Weight: 73
# 1.8
# 33.112216
# The BMI is: 10.219819753086417
# UnderWeight - Consult A Nutritionist
