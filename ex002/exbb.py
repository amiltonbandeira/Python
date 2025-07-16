#A program to sum what the user types
n1 = input("Type Something \n")
n2 = input("Type Another thing \n")
sum = int(n1,36) + int(n2,36)
print("The sum between {} and {} is {}\nAnd the proper string is {}\n".format(n1,n2,sum,n1+n2))