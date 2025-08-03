city = input("Type the name of a city: \n")
city = city.upper()
organized_city = city.split()
if organized_city[0] == "SANTO":
    print("The city starts with SANTO \n")
else:
    print("The city does not start with SANTO \n")