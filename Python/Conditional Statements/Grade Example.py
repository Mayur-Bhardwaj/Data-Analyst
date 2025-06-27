# Enter Students marks and tell the grade.

grade_input = float(input("Please Enter your marks here: "))

if (grade_input >=90 and grade_input <=100) :
    print("A1")
elif ( grade_input >=75 and grade_input < 90):
    print("A2")
elif ( grade_input >=60 and grade_input <75):
    print("B1")
elif ( grade_input >=50 and grade_input <60):
    print("B2")
elif( grade_input >=40 and grade_input <50):
    print("C")
elif (grade_input >= 33 and grade_input <40):
    print("D")
elif (grade_input < 33):
    print("F")
else:
    print("Sorry You Enter Wrong Number, Please Re-enter !!")


# Output:

# Please Enter your marks here: 92
# A1

# Please Enter your marks here: 85
# A2

# Please Enter your marks here: 70
# B1

# Please Enter your marks here: 59
# B2

# Please Enter your marks here: 45
# C

# Please Enter your marks here: 38
# D

# Please Enter your marks here: 10
# F

# Please Enter your marks here: 101
# Sorry You Enter Wrong Number, Please Re-enter !!

# Please Enter your marks here: 80.5
# A2

# Please Enter your marks here: 67.5
# B1