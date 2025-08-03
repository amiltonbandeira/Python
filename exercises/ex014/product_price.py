price = float(input("What is the product price ? R$\n"))
discount = (5/100)* price
new_price = price - discount
print("The product that used to cost R${}, in promo with discount of 5% will cost R${}\n".format(price,new_price))
