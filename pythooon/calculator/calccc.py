from functions import add, subtract, multiply, divide

a = float(input("Enter first number: "))
b=float(input("Enter second number: "))

c=input("Enter operation (+, -, *, /): ")

if c == "+":
    print(add(a, b))
elif c == "-":
    print(subtract(a, b))
elif c == "*":
    print(multiply(a, b))
elif c == "/":
    print(divide(a, b))
else:
    print("Invalid operation")

