num_1 = input("Enter first number: ")
sing = input("Enter sing: ")
num_2 = input("Enter second number: ")

if sing == "+":
    print(int(num_1) + int(num_2))
elif sing == "-":
    print(int (num_1) - int (num_2))
elif sing == "/":
    print(int (num_1) / int (num_2))
elif sing == "*":
    print(int (num_1) * int (num_2))
else :
    print("Wrong sing!")
 