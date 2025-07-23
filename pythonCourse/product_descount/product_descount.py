price=float(input("What is the price of the product ? Kz\n"))
tax = ((5/100) * price)
product = (price - tax)
print("The product that used to be {:.2f}Kz, in the promo of 5% what is  {:.2f}Kz  is  now being {:.2f} Kz\n".format(price,tax,product))