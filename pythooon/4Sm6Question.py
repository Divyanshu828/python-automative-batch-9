numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
# Output: [1, 4, 9, 16, 25]


students =[100, 90, 80, 70, 60,50,40,30,0]

pass_students = [i if i>=60 else "failed" for i in students]
print(pass_students)