print("*"*50)
n = int(input("Type the number of student´s : \n"))
print("*"*50)
for i in range(n):
    name = input("Type student name: \n")
    n1 = float(input("Type student´s first classification: \n"))
    n2 = float(input("Type student´s second classification : \n"))
    média = ( n1 + n2 ) / 2
    id = i
print(name)
for i in range(n):
    print("The student {} with {} as first classification , {} as second classification , {} is the media and student id is {}\n".format(name,n1,n2,média,id))


