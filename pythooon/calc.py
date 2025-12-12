def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

a = float(input("Enter first: "))
b = float(input("Enter second: "))
op = input("Enter + - * / : ")

if op == "+": print(add(a,b))
elif op == "-": print(sub(a,b))
elif op == "*": print(mul(a,b))
elif op == "/": print(div(a,b))
else: print("Invalid")
