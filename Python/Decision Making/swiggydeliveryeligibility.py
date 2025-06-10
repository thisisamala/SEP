service=int(input("Is the user's location within the serviceable area? default(0 for no/1 for yes "))
amount=float(input("The total amount in rupees :"))
if(service==bool(0) and amount<200):
    print("Delivery is not available for your order" )
else:
    print("Your order will be delivered")
