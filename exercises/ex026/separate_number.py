number = int(input("Type a number: \n"))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print("Analysing number {}".format(number))
print("Unit: {}".format(u))
print("Dezena: {}".format(d))
print("Century: {}".format(c))
print("Milhar: {}".format(m))

#right way