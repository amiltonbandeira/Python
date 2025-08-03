salary = float(input("Type how much you earn "))
increase = 0
if salary > 1250:
    increase = (10/100) * salary
else:
    increase = (15/100) * salary
print("Your increase is {}".format(salary + increase))
