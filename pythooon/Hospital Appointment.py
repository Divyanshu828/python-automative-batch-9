# HOSPITAL APPOINTMENT SYSTEM


doctors = {                                   # Dictionary storing doctors and their slots
    "Dr. Smith": ["10:00", "11:00", "12:00"], # Slots for Dr. Smith
    "Dr. John": ["2:00", "3:00", "4:00"]      # Slots for Dr. John
}

appointments = []                             # List to store booked appointments


def view_doctors():                           # Function to display doctors
    print("\nAvailable Doctors:")             # Heading
    for doctor in doctors:                    # Loop through dictionary keys
        print(doctor)                         # Print doctor name


def check_slots():                            # Function to check slots
    doc = input("\nEnter doctor name: ")      # Take doctor name from user
    if doc in doctors:                        # Check if doctor exists
        print("Available slots:")             # Heading
        for slot in doctors[doc]:             # Loop through selected doctor's slots
            print(slot)                       # Print each slot
    else:
        print("Doctor not found")              # Error message


def book_appointment():                       # Function to book appointment
    name = input("\nEnter patient name: ")    # Patient name
    age = input("Enter age: ")                # Patient age
    doc = input("Enter doctor name: ")        # Doctor name
    time = input("Enter time slot: ")         # Time slot

    if doc in doctors and time in doctors[doc]:   # Validate doctor and slot
        doctors[doc].remove(time)                 # Remove booked slot

        appointments.append({                     # Save appointment details
            "Patient": name,                      # Patient name
            "Age": age,                           # Patient age
            "Doctor": doc,                        # Doctor name
            "Time": time                          # Appointment time
        })

        print("Appointment booked successfully")  # Success message
    else:
        print("Invalid doctor or time slot")      # Error message


def view_appointments():                       # Function to view patient details
    if not appointments:                       # Check if list is empty
        print("\nNo appointments booked yet.") # Message if no data
    else:
        print("\nPatient Appointments:")       # Heading
        for appt in appointments:              # Loop through appointments
            print(                              # Print appointment info
                "Patient:", appt["Patient"],
                "| Age:", appt["Age"],
                "| Doctor:", appt["Doctor"],
                "| Time:", appt["Time"]
            )


while True:                                   # Infinite loop for menu
    print("\n--- Hospital Appointment System ---")
    print("1. View Doctors")                   # Menu option 1
    print("2. Check Available Slots")          # Menu option 2
    print("3. Book Appointment")               # Menu option 3
    print("4. View Patient Details")           # Menu option 4
    print("5. Exit")                           # Menu option 5

   

    choice = input("Enter your choice: ")      # User input

    if choice == "1":
        view_doctors()                         # Call view doctors
    elif choice == "2":
        check_slots()                          # Call check slots
    elif choice == "3":
        book_appointment()                     # Call book appointment
    elif choice == "4":
        view_appointments()                    # Call view appointments
    elif choice == "5":
        print("Thank you. Program exited.")    # Exit message
        break                                 # Stop the loop
    else:
        print("Invalid choice. Try again.")    # Invalid input
