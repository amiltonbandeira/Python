money = float(input("How much is the money employee receive? R$\n"))
increment = (15/100) * money
salary = money + increment
print("An employee that used to receive R${} , with an increment of 15%, starts to receive R${:.2f}".format(money,salary))