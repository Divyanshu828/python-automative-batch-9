import re

class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def get_number(self):
        # Find number from student ID using regex
        num = re.search(r'\d+', self.student_id)
        return int(num.group())

    def is_even(self):
        # Check if the student ID number is even
        return self.get_number() % 2 == 0


# List of student IDs
student_ids = [
    "std_001", "std_002", "std_003", "std_004", "std_005",
    "std_006", "std_007", "std_008", "std_009", "std_010"
]

even_students = []
odd_students = []

# Create Student objects and divide them
for sid in student_ids:
    s = Student(sid)

    if s.is_even():
        even_students.append(sid)
    else:
        odd_students.append(sid)

# Print result
print("Even ID Students (First queue):")
print(even_students)

print("\nOdd ID Students (Second queue):")
print(odd_students)

a=input("enter user Id:")
x=Student(a)
if x.is_even():
    print("first queue")
else:
    print("second queue")
