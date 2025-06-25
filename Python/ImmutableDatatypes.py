# Immutable Datatypes - Numeric (Int, Float, Complex), String, Boolean, Tuple

a = 10
print(a)       # 10
print(id(a))   # 2759492370960

a = a+5   
print(a)       # 15
print(id(a))   # 1407259837104      Here the location is also changed

# Note:- In immutable data types when we change the value of variable then the memory location is also changed.


# Complex No.

c= 3+7j
print(c)      # (3+7j)
print(id(c))  # 1766197336016

# T print real and imaginary term
print(c.real)   #3.0
print(c.imag)   # 7.0

str = "Python"
print(str)       # Python
print(id(str))   # 2233612126768

str = "Python Data Analyst"
print(str)      # Python Data Analyst
print(id(str))  # 2492045155328
# The memory allocation is also changed
