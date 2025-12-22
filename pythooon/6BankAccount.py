class BankAccount:

#initialisation

def init(self,account_number,customer_name, initial_balance=@.0):

self.account_number=account_number #123
self.customer_name=customer_name #alice
self.balance=initial_balance #50.0

def deposit(self, amount): self.balance+=amount #70
def withdraw(self, amount): self.balance-=amount#6e T

account1-BankAccount("123", "ALice", 50.00)
account1.deposit(20)
account1.withdraw(10)