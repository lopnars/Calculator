print("Select an operation to preform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operator = input()

if operator == "1":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)) )
elif operator == "2":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) - int(num2)) )
elif operator == "3":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) * int(num2)) )
elif operator == "4":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The sum is " +  str(int(num1) / int(num2)) )
else:
    print("Invalid Entry")