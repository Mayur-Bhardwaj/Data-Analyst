# Write a program that takes the length of 3 sides of a triangle as input and determine the type of triangle.
# Equilateral(all sides equal), Isosceles(2 sides equal) or Scalene Triangle(all side different)
# If the input value do not form a valid triangle(sum of any 2 sides is not greater than 3rd side), display "Invalid Triangle".


length_1 = float(input("Please Enter here length_1 of Triangle: "))
length_2 = float(input("Please Enter here length_2 of Triangle: "))
length_3 = float(input("Please Enter here length_3 of Triangle: "))

if(length_1 + length_2 > length_3 or length_1 + length_3 > length_2 or length_2 + length_3 > length_1):
    # Check for Equilateral Triangle
    if (length_1 == length_2 == length_3):
        print("Equilateral Triangle")
    elif (length_1 == length_2 or length_2 == length_3 or length_3 == length_1):
        print("Isosceles Triangle")
    else:
        print("Scalen Triangle")
else:
    print("Invalid Triangle")



# Output:
# Please Enter here length_1 of Triangle: 3
# Please Enter here length_2 of Triangle: 3
# Please Enter here length_3 of Triangle: 3
# Equilateral Triangle

# Please Enter here length_1 of Triangle: 7
# Please Enter here length_2 of Triangle: 5
# Please Enter here length_3 of Triangle: 7
# Isosceles Triangle

# Please Enter here length_1 of Triangle: 2
# Please Enter here length_2 of Triangle: 4
# Please Enter here length_3 of Triangle: 8
# Scalen Triangle