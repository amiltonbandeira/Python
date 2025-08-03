distance = float(input("Type the distance of your travel km: \n"))
price = 0
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print("The price for your travel is R${}".format(price))