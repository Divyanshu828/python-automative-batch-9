from Validator.validatorfun import validate_email, validate_mobile

email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")

if validate_email(email):
    print("---------Valid Email ID--------------")
else:
    print("---------Invalid Email ID------------")

if validate_mobile(mobile):
    print("---------Valid Mobile Number----------")
else:
    print("---------Invalid Mobile Number--------")
