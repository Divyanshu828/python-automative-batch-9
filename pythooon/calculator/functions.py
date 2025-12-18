def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def generate_report(marks):
    if marks <60:
        return "Fail"
    else:
        return "Pass"

def calculate_percentage(total_marks, total_subjects):   # Function to calculate percentage
    return (total_marks / (total_subjects * 100)) * 100