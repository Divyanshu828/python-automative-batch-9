while True:
    name=input("Enter your name: ")
    if name!="":
        break

phone_number="123-456-7890"
for digit in phone_number:
    if digit=="-":
        continue
    print(digit,end=" ")