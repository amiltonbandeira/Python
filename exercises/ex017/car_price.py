day = int(input("How manny days you got the car ? \n"))
day *= 60
km = int(input("How manny kilometers run? \n"))
km *= 0.15
total_to_pay = day +  km
print("The total to pay is R${}".format(total_to_pay))