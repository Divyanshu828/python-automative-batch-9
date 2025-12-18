# G6. Prime Number Finder
# Write a program that takes a number as input and checks whether it is a prime number
#  using loops. Use the break statement when a factor is found.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:  # factor found
            print("Not a Prime Number")
            break
    else:
        print("Prime Number") # no factors found
else:
    print("Not a Prime Number") # numbers less than or equal to 1 are not prime


# Example usage:

# Enter a number: 29
# Prime Number
# Enter a number: 15
# Not a Prime Number
