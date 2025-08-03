import random
import time
print("Let´s start")
computer_number = random.randint(0, 5)
number = int(input("Now I thought in a number from 0 - 5 , try to guess which: \n"))
print("Processing")
time.sleep(4)
if number == computer_number:
    print("You won {} is the number I though, Congrats\n")
else:
    print("You loose , {} is not the number I thought")
