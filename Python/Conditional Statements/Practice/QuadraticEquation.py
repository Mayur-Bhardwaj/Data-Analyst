# Write a program to solve the Quadratic Equation of the form ax^2+bx+c=0. Take the codfficient a,b,c as 
# input from the user and calculate the discriminant.Based on Discriminent, determine whether the equation
# has real and distinct roots, real and equal roots, or imaginary roots. Display the roots or an appropriate
# message for imaginary roots.

# D --> Discriminent      D =b^2-4ac
# X --> (-b+√D)/2a          X --> (-b-√D)/2a
# √D = 0 {2 Equal Roots of the equation}
# √D < 0 {No Roots Exists of the equation}
# √D > 0 {Real Roots of the equation}

print("Enter the Coefficient of ax^2+bx+c ")
a=int(input("Coefficient of a: "))
b=int(input("Coefficient of b: "))
c=int(input("Coefficient of c: "))

# Calc Discriminent

dis = (b*b)-(4*a*c)
print(f"Discriminent: {dis}")

if dis>0:
    print("This equation has real and equal roots")
    root1= (-b + dis**0.5)/(2*a)
    root2= (-b - dis**0.5)/(2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif dis == 0:
    print("This equation have equal roots")
    root1= (-b)/(2*a)
    root2= (-b)/(2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    print("This equation have imaginary roots")


# Output:
# Enter the Coefficient of ax^2+bx+c 
# Coefficient of a: 3
# Coefficient of b: 7
# Coefficient of c: 2
# Discriminent: 25
# This equation has real and equal roots
# Root 1: -0.3333333333333333
# Root 2: -2.0

# Enter the Coefficient of ax^2+bx+c 
# Coefficient of a: 2
# Coefficient of b: 4
# Coefficient of c: 6
# Discriminent: -32
# This equation have imaginary roots