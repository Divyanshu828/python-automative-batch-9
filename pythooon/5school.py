# List of 20 students (first name and surname)
students = [
    "Rahul Sharma", "Amit Kumar", "Rahul Verma", "Sneha Singh",
    "Amit Gupta", "Priya Mehta", "Rohit Yadav", "Neha Patel",
    "Ankit Jain", "Pooja Agarwal", "Neha Sharma", "Vikas Malhotra",
    "Ravi Singh", "Sonal Gupta", "Ankit Verma", "Kiran Joshi",
    "Deepak Mishra", "Ravi Kumar", "Suman Das", "Pooja Verma"
]

name_dict = {}                     # Dictionary to store first name as key and surnames as values

for full_name in students:         # Loop through each student name in the list
    parts = full_name.split()      # Split full name into first name and surname
    first_name = parts[0]          # Extract first name
    last_name = parts[1]           # Extract surname

    if first_name in name_dict:    # Check if first name already exists in dictionary
        name_dict[first_name].add(last_name)   # Add surname to the set (avoids duplicates)
    else:
        name_dict[first_name] = {last_name}    # Create a new set with the surname

print("Students with same first name but different surname:\n")

for first_name, surnames in name_dict.items():  # Loop through dictionary items
    if len(surnames) > 1:       # Check if more than one surname exists
        print(first_name, "→", list(surnames))  # Print first name with different surnames

print("Unique Students List:\n")
unique_students = set(students)   # Convert list to set to remove duplicates
for student in unique_students:    # Loop through unique students
    print(student)                 # Print each unique student name