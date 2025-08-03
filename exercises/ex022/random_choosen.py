import random
name = []
for i in range(4):
    name.append(input("Type the students name: \n"))
print("The student to clean the board is {}".format(random.choice(name)))