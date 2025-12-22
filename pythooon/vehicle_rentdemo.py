class Vehicle:

    def _init_(self, vehicle_id, vehicle_type, rent_per_day):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day
        self.is_rented = False

    def rent_vehicle(self, days):
        if self.is_rented:
            print("Vehicle is already rented. Cannot rent again.")
            return

        self.is_rented = True
        total_rent = self.calculate_rent(days)
        print(f"Vehicle rented for {days} days.")
        print(f"Total rent: {total_rent}")

    def return_vehicle(self):
        if not self.is_rented:
            print("Vehicle is not currently rented.")
            return

        self.is_rented = False
        print("Vehicle has been returned successfully.")

    def calculate_rent(self, days):
        return self.rent_per_day * days


# Create vehicle ONCE
vh = Vehicle("1", "Sedan", 200)

while True:
    print("\n--------- Vehicle Rental System --------")
    print("1 - Rent Vehicle")
    print("2 - Return Vehicle")
    print("3 - Calculate Rent")
    print("4 - Exit")

    op = int(input("Select action: "))

    if op == 1:
        days = int(input("Enter number of days: "))
        vh.rent_vehicle(days)

    elif op == 2:
        vh.return_vehicle()

    elif op == 3:
        days = int(input("Enter number of days: "))
        print("Total rent:", vh.calculate_rent(days))

    elif op == 4:
        print("Exiting system.")
        break

    else:
        print("Invalid option.")