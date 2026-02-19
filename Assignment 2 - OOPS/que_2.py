# Create methods in the BankAccount class to deposit and withdraw money from the account, and to calculate the interest based on the interest rate and the account balance. Interest = balance * interest_rate 
class BankAccount:
        Account_number=213654212789425
        balance=20000
        interest_rate=8
        def __init__(self, name):
                self.name=name
        def deposite(self,amount):
                self.amount=amount
                new_balance=self.balance + amount
                print(f"your New Balance after Deposite is : {new_balance}")
        def withdraw(self,amount):
                self.amount=amount
                new_balance=self.balance - amount
                print(f"Your New Balance after Withdraw is : {new_balance}")
        def interest(self):
                Interest = self.balance * self.interest_rate 
                print(f"Interest Based Rate is {Interest}")

name= input("Please Enter your Name : ")
person= BankAccount(name)
print(f"Welcome {person.name}")
print(f"Your Account Number is {person.Account_number}")
print(f"Your Account Balance is {person.balance}")
print(f"Your Account Interest Rate is {person.interest_rate}")