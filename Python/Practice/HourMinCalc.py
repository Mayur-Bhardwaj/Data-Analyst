# Ask user for two numbers and raise one to the power of another. Ask the user to enter the time in seconds and convert it into hours, minutes & seconds.

second_input = int(input("Please enter the time in seconds: "))

hours = second_input//3600      # Because in 1 hour 3600 seconds.
remaining_second = second_input%3600  # Remaining seconds after calculating hours.
minutes = remaining_second //60
seconds = remaining_second%60

print(f"{second_input} value = {hours}, {minutes} minute, {seconds} second.")

#Output:
# Please enter the time in seconds:  3600
# 3600 value = 1, 0 minute, 0 second.

# Please enter the time in seconds:  6789
# 6789 value = 1, 53 minute, 9 second.

#3783  divide by 3600 to calc hour, the rem of 3600 is divide by 60 to cal min and the remainder after divide by
# 60 sec