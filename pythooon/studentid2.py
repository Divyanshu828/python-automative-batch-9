class studentid2(Student):
    super().__init__(student_id)

a=input("enter user Id:")
x=Student(a)
if x.is_even():
    print("first queue")
else:
    print("second queue")