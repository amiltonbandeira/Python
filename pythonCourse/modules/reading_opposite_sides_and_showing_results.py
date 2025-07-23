from math import pow
opposite_cathet = float(input("Type Opposite Cathet Of the triangle: \n"))
adjacent_cathet = float(input("Type Adjacent Cathet Of the triangle: \n"))
hypotenuse = (pow(opposite_cathet, 2) + pow(adjacent_cathet, 2))
print("The Compriment of the hypotenuse of the right triangle is {}".format(hypotenuse))
