# Input the Principal, rate of interest, and time in years, then calculate and print the Simple Interest.

principal = float(input("Enter the Principal: "))
rate_of_interest = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the time: "))

SI= (principal*rate_of_interest*time)/100

print(f"The SI is {SI}")

# Output:
# Enter the Principal:  23
# Enter the Rate of Interest:  2
# Enter the time:  2
# The SI is 0.92

