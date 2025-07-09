
# RANGE in FOR Loops: It is a function that is used to generate a sequence of number.
# RANGE will print index-1.
# Syntax: Syntax. range(start, stop, step) or range(start, end, jump). Here start and jump/step are optional but end is compulsory.
# Suppose there is a lucky draw result and we want every 4th number is winner.
# list = [1,7,9,11,15,35,4,9,3,4,52,98,23,87,100]

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Print range from 5 to 25

for i in range(5,26):
    print(i)

# Output:
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25

for i in range(1,20,2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

for i in range(-100,100,10):
    print(i)

# Output:
# -100
# -90
# -80
# -70
# -60
# -50
# -40
# -30
# -20
# -10
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
