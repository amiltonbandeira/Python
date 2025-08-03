from math import sqrt , pow
c_o = float(input("Type the opposite side of the retangular triangle: \n "))
c_a = float(input("Type the adjacent side of the retangular triangle: \n"))
h = sqrt(pow(c_o,2) + pow(c_a,2))
print("For opposite side {} and adjacent side {}, the hypotenuse is {:.2f}".format(c_o,c_a,h))
