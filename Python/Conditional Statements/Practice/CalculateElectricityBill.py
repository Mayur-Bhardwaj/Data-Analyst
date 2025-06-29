# Write a program to calculate an electricity bill based on the number of units consumed, using the following rate slabs:
# 1. ₹5 per units for the first 100 units.
# 2. ₹7 per units for the next 200 units (101 to 300 units).
# 3. ₹10 per units for any units above 300.
# 4. If the total bill exceeds ₹5,000, add 10% surcharge to the total bill.

units = int(input("Please Enter here your consumed units: "))

if( units <0):
    print("Please Enter Valid Unit")
else:
    print("Bill Summary.")
    slab1 = 5
    slab2 = 7
    slab3 = 10
    if units <=100:
        total_Bill = units*slab1
        print(f"The total Bill : {units} units {slab1} = {total_Bill}")
    elif units <=300:
        total_Bill = (100*slab1)+((units-100)*slab2)
        print(f"The total Bill : (100 Units* {slab1}) +  ({units-100}* {slab2})= {total_Bill}")
    else:
        total_Bill = (100*slab1)+(200*slab2)+((units-(100+200))*slab3)
        print(f"The total Bill Calculation: (100 Units* {slab1}+ (200 Units* {slab2}) + ({units-100-200}*{slab3} = {total_Bill}))")

if total_Bill > 5000:
    surcharge = total_Bill*0.10             # 10% of total_Bill if bill is more than 5000
    total_Bill = total_Bill + surcharge     #Now the new bill is initial Bill(total_Bill) + Surcharge.
    print(f"Surcharge: {surcharge}")

print(f"Total Electricity Bill for {units} is: {total_Bill}")

 # Output:
# Please Enter here your consumed units: 60
# Bill Summary.
# The total Bill : 60 units 5 = 300
# Total Electricity Bill for 60 is: 300

# Please Enter here your consumed units: 285
# Bill Summary.
# The total Bill : (100 Units* 5) +  (185* 7)= 1795
# Total Electricity Bill for 285 is: 1795

# Please Enter here your consumed units: 800
# Bill Summary.
# The total Bill Calculation: (100 Units* 5+ (200 Units* 7) + (500*10 = 6900))
# Surcharge: 690.0
# Total Electricity Bill for 800 is: 7590.0