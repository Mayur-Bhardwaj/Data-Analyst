# A retail store wants to implement a discount system to enhance customer satisfaction and loyalty. 
# The discount varies based on the type of customer(Regular, Premium, VIP) and the total purchase amount.
# The system must determine the applicable discount and calculate the final price after applying the discount.
# Here the cashier will enter the customer type and purchase amt and, you should store in o/p[cx type, amt purchase, discount applicable, final amt]
# Discount will be given on the basis of following conditions:
# 1. Regular Customer:
# --> No discount for purchase below $100.
# --> 5% discount for purchase b/w $100 & $500(inclusive).
# --> 10% discount for purchase above $500.
# 2. Premium Customer:
# --> 10% discount for purchase below $500. 
# --> 15% discount for purchase above $500. 
# 3. VIP Customer:
# --> 20% discount for purchase below $1000. 
# --> 30% discount for purchase above $1000.
 

customer_type = input("Please Enter Customer Type: ")
purchase_amount = float(input("Please Enter Purchase Amount: "))

discount = 0

if customer_type == "Regular":
    if purchase_amount < 100:
       discount = 0
    # elif purchase_amount >=100 and purchase_amount <= 500:
    elif purchase_amount <= 500:
         discount = 5
    else: 
         discount = 10
         
    discount_amount = (discount /100) * purchase_amount   # Convert the discount percentage into amt
    final_price = purchase_amount - discount_amount


    print("---------- PURCHASE SUMMARY ----------")
    print(f"Customer Type: {customer_type}")
    print(f"Purchase Amount: {purchase_amount}")
    print(f"Discount: {discount}%")
    print(f"Final Amoount: {final_price}")


elif customer_type == "Premium":
    if purchase_amount <= 500:
        discount = 10
    else:
        discount = 15
        
    discount_amount = (discount /100) * purchase_amount   # Convert the discount percentage into amt
    final_price = purchase_amount - discount_amount


    print("---------- PURCHASE SUMMARY ----------")
    print(f"Customer Type: {customer_type}")
    print(f"Purchase Amount: {purchase_amount}")
    print(f"Discount: {discount}%")
    print(f"Final Amoount: {final_price}")

    
elif customer_type == "VIP":
    if purchase_amount <= 1000:
        discount = 20
    else: 
        discount = 30
        
    discount_amount = (discount /100) * purchase_amount   # Convert the discount percentage into amt
    final_price = purchase_amount - discount_amount


    print("---------- PURCHASE SUMMARY ----------")
    print(f"Customer Type: {customer_type}")
    print(f"Purchase Amount: {purchase_amount}")
    print(f"Discount: {discount}%")
    print(f"Final Amoount: {final_price}")

        
else:
    print("Invalid Customer !!")


# Output:
# Please Enter Customer Type: Regular
# Please Enter Purchase Amount: 400
# ---------- PURCHASE SUMMARY ----------
# Customer Type: Regular
# Purchase Amount: 400.0
# Discount: 5%
# Final Amoount: 380.0

# Please Enter Customer Type: Premium
# Please Enter Purchase Amount: 780
# ---------- PURCHASE SUMMARY ----------
# Customer Type: Premium
# Purchase Amount: 780.0
# Discount: 15%
# Final Amoount: 663.0

# Please Enter Customer Type: VIP
# Please Enter Purchase Amount: 5000
# ---------- PURCHASE SUMMARY ----------
# Customer Type: VIP
# Purchase Amount: 5000.0
# Discount: 30%
# Final Amoount: 3500.0

# Please Enter Customer Type: Normal
# Please Enter Purchase Amount: 200
# Invalid Customer !!