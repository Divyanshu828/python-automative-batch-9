print("Division of two numbers")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num2!=0:
    result=num1//num2
    print("Result:", result) #results will be in integer form(no decimal)
else:
    print("Error: Division by zero is not allowed.")