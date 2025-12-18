from functions import multiply, divide

print("------SIMPLE INTEREST CALCULATOR--------")

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (in %): "))
t = float(input("Enter the time period (in years): "))

# Simple Interest = (P × R × T) / 100

step1 = multiply(p, r)        # P × R
step2 = multiply(step1, t)   # (P × R) × T
si = divide(step2, 100)      # Final Simple Interest

print("Simple Interest is:", si)
