width = float(input("Wall width: \n"))
height = float(input("Wall height: \n"))
area = width * height
qty = area/2
print("Your wall has dimension of {}x{} and your area is of {}m".format(width,height,area))
print("To paint this wall, you will need {}l of paint".format(qty))