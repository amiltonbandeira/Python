import math
angle = float(input("Type an angle: \n"))
angle = math.radians(angle)
cos = math.cos(angle)
sen = math.sin(angle)
tan = math.tan(angle)
print("The tangent of {:.2f} is {:.2f}".format(angle,tan))
print("The Sen of {:.2f} is {:.2f}".format(angle,sen))
print("The Cos of {:.2f} is {:.2f}".format(angle,cos))