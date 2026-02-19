# Create a BankAccount class with attributes account_number, balance, and interest_rate.

class BankAccount:
        Account_number=213654212789425
        balance="20,000"
        interest_rate=50
        def __init__(self, name):
                self.name=name

name= input("Please Enter your Name : ")
person= BankAccount(name)
print(f"Welcome {person.name}")
print(f"Your Account Number is {person.Account_number}")
print(f"Your Account Balance is {person.balance}")
print(f"Your Account Interest Rate is {person.interest_rate}")
