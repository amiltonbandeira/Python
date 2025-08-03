import random
elements = []
for i in range(4):
    elements.append(input("Type the name of the participants: \n"))
random.shuffle(elements)
print(elements)