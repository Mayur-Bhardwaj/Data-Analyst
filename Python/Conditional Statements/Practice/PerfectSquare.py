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
