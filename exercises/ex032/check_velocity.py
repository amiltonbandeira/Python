v = float(input("Type your current velocity km/h:\n"))
if v > 80:
    print("You need to pay, very fast!!")
    v -= 80
    payment = v * 7.00
    print("You need to pay R${} ".format(payment))