print("1 - add")

print("2 - sub")

print("3 - multiply")

print("4 - divide")

print("5-square")

print("6 - cubee")

print("7 - remainder")

option =int(input("enter the choose operations:")) if (option in (1,2,3,4,5,6,7)): # using tuples concept

if (option ==1):

num1 = int(input("enter the first number :"))

num2 = int(input("enter the second number :")) result =num1+num2

if (option ==2):

num1 = int(input("enter the first number :"))

num2 = int(input("enter the second number :"))

result =num1-num2

if (option ==3):

num1 = int(input("enter the first number :"))

num2 = int(input("enter the second number :"))

result =num1*num2

if (option ==4):

num1 = int(input("enter the first number :"))

num2 = int(input("enter the second number :")) result =num1/num2

if (option ==5):

num1 = int(input("enter the first number :")) result =num1*num1

if (option ==6):

num1 = int(input("enter the first number :"))

result =num1*num1*num1

if (option ==7):

num1 = int(input("enter the first number :")) num2 = int(input("enter the second number :")) result =num1%num2

print("the result of the opertion is:", result)

else:

print("invalid opertion entered ")