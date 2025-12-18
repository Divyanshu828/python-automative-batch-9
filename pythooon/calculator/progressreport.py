from functions import generate_report, calculate_percentage

print("PROGRESS REPORT FUNCTION")

subjects = ["Maths", "Science", "English", "History", "Geography"]
total_marks = 0                              # To store sum of all marks

for subject in subjects:                     # Loop through subjects
    marks = int(input(f"Enter the marks obtained in {subject}: "))
    total_marks += marks                    # Add marks to total
    result = generate_report(marks)         # Pass/Fail check
    print(f"Result: {result}")

percentage = calculate_percentage(total_marks, len(subjects))  # Calculate percentage
print(f"\nTotal Percentage: {percentage:.2f}%")
