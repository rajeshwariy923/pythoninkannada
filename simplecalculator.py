print("Simple Calculator")
print("Select an Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("0. End the Program")

while True:
    operation = int(input("Enter choice(1/2/3/4/0) >>  "))

    if operation not in ['1', '2', '3', '4', '0']:
        print("invalid operation try again")

    num1 = float(input("Enter num1>>  "))
    num2 = float(input("Enter num2>>  "))

    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    elif operation==0:
        break
    else:
        print("Invalid Option! Please Try Again")




