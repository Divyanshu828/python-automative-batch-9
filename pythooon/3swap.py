def get_numbers():
    a, b = map(int, input("Enter two numbers (comma separated): ").split(","))
    return a, b

def show_menu():
    print("\n1. Max")
    print("2. Min")
    print("3. Swap")

a, b = map(int, input("Enter two numbers").split(","))

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Maximum:", max(a, b))

elif choice == 2:
    print("Minimum:", min(a, b))

elif choice == 3:
    a, b = b, a
    print("After swapping:", a, b)

else:
    print("Invalid choice")
