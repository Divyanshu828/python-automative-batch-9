class BankAccount:
    
    # Constructor: initializes account details
    def __init__(self, name, age, principal, time):
        try:
            # assigning values to instance variables
            self.name = name
            self.age = int(age)
            self.principal = float(principal)
            self.time = float(time)
            self.rate = 8   # interest rate fixed at 8%
            
            print("Account created successfully for", self.name)
        
        except ValueError:
            # handles wrong data type input
            print("Invalid input while creating account")
        
        finally:
            # this block always executes
            print("Initialization process completed\n")

    # Definition to check whether the account holder is a senior citizen
    def check_senior_citizen(self):
        try:
            # checking age condition
            if self.age >= 60:
                print("Senior citizen verified")
            else:
                # raising exception if age is less than 60
                raise ValueError("Not a senior citizen")
        
        except ValueError as e:
            print(e)
        
        finally:
            # always executes
            print("Age verification completed\n")

    # Definition to calculate Compound Interest
    def calculate_ci(self):
        try:
            # CI applicable only for senior citizens
            if self.age < 60:
                raise ValueError("CI applicable only for senior citizens")

            # real compound interest formula
            amount = self.principal * (1 + self.rate / 100) ** self.time
            ci = amount - self.principal

            # printing result inside the definition
            print("Total Amount after CI:", amount)
            print("Compound Interest:", ci)

        except ValueError as e:
            print(e)
        
        finally:
            # always executes
            print("CI calculation process completed\n")

    # Additional definition instead of display_details
    # Shows account summary
    def show_account_summary(self):
        try:
            print("Account Summary")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Principal:", self.principal)
            print("Time:", self.time, "years")
            print("Rate:", self.rate, "% per annum")
        
        except AttributeError:
            # handles missing attributes
            print("Unable to fetch account details")
        
        finally:
            # always executes
            print("Summary displayed successfully\n")


# creating BankAccount object
acc = BankAccount("Divyanshu", 65, 10000, 2)

# calling different definitions
acc.check_senior_citizen()
acc.calculate_ci()
acc.show_account_summary()
