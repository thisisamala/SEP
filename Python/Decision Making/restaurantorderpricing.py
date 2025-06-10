subtotal=float(input("Enter the total price"))
tax=subtotal*0.01
discountrate=0.05
discount=0
if(subtotal>100.0):
    discount=subtotal*discountrate
    finalprice=subtotal+tax-discount
    print("Subtotal :",subtotal)
    print("Tax :",tax)
    print("Discount :",discount)
    print("Final Price",finalprice)
else:
    finalprice=subtotal+tax
    print("Subtotal :",subtotal)
    print("Tax :",tax)
    print("Discount :",discount)
    print("Final Price",finalprice)