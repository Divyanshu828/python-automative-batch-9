# 6️⃣ Vehicle Rental System
# Use Case:
# Create a Vehicle class.
# Properties:
# vehicle_id
# vehicle_type
# rent_per_day
# is_rented
# Behaviors:
# rent_vehicle(days)
# return_vehicle()
# calculate_rent(days)
# Task:
# Do not allow renting if vehicle is already rented.

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type.lower()
        self.is_rented = False

        if self.vehicle_type == "car":
            self.rent_per_day = 1500
        elif self.vehicle_type == "bike":
            self.rent_per_day = 500
        elif self.vehicle_type == "truck":
            self.rent_per_day = 3000
        else:
            raise ValueError("Invalid vehicle type")

    def rent_vehicle(self, days):
        try:
            if self.is_rented:
                raise Exception("Vehicle is already rented")

            if days <= 0:
                raise ValueError("Number of days must be greater than zero")

            self.is_rented = True
            total_rent = self.calculate_rent(days)

            print(f"Vehicle ID: {self.vehicle_id}")
            print(f"Vehicle Type: {self.vehicle_type.capitalize()}")
            print(f"Rented for {days} days")
            print(f"Rent per day: ₹{self.rent_per_day}")
            print(f"Total Rent: ₹{total_rent}")

        except Exception as e:
            print("Error:", e)

        finally:
            print("Rent process completed.\n")

    def calculate_rent(self, days):
        return self.rent_per_day * days

    def return_vehicle(self):
        try:
            if not self.is_rented:
                raise Exception("Vehicle is not currently rented")

            self.is_rented = False
            print("Vehicle returned successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            print("Return process completed.\n")


vehicles = {}   # Stores vehicle_id : Vehicle object

print("----- Vehicle Rental System -----")

while True:
    try:
        print("\n1. Rent Vehicle")
        print("2. Return Vehicle")
        print("3. Exit")

        op = int(input("Select action: "))

        if op == 1:
            vehicle_id = input("Enter vehicle ID: ")

            # Create vehicle only if it does not exist
            if vehicle_id not in vehicles:
                vehicle_type = input("Enter vehicle type (car/bike/truck): ")
                vehicles[vehicle_id] = Vehicle(vehicle_id, vehicle_type)

            days = int(input("Enter number of days: "))
            vehicles[vehicle_id].rent_vehicle(days)

        elif op == 2:
            vehicle_id = input("Enter vehicle ID: ")

            if vehicle_id in vehicles:
                vehicles[vehicle_id].return_vehicle()
            else:
                print("Error: Vehicle not found.")

        elif op == 3:
            print("Exiting system.")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
