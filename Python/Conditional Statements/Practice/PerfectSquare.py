# Creates a program that takes an integer and ckassifies it based on specific properties:
# 1. If the number is perfect square and even then prints "Perfect Square & Even",
# 2. If the number is perfect square and odd then prints "Perfect Square & Odd",
# 3. If the number is not perfect square  then prints "Not a Perfect Square",
# Incorporate checks to handle edge cases like negative number or zero.


number = int(input("Enter an integer: "))

if number < 0:
    print("Negative numbers cannot be perfect squares.")
else:
    if number == 0:
        print("0 is a Perfect Square & Even")
    else:
        if number == 1*1:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 2*2:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 3*3:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 4*4:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 5*5:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 6*6:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 7*7:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 8*8:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 9*9:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        elif number == 10*10:
            if number % 2 == 0:
                print("Perfect Square & Even")
            else:
                print("Perfect Square & Odd")
        else:
            print("Not a Perfect Square")


# Best Code

# (number**0.5)  //Under Root


number = int(input("Please Enter a Number: "))
sqrt = int(number**0.5)**2

if(number<0):
    print("Please Enter the Positive Real Number")
else:
    if(number == sqrt and number%2==0):
        print(f"{number} is Perfect Even Number")
    elif(number == sqrt and number%2!=0):
        print(f"{number} is Perfect Odd Number")
    else:
        print("The number is not a Perfect Square.")
    

# Output:
# Please Enter a Number: 100
# 100 is Perfect Even Number

# Please Enter a Number: 49
# 49 is Perfect Odd Number

# Please Enter a Number: 98
# The number is not a Perfect Square.
