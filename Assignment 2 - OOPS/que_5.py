# Override the withdraw method in the SavingsAccount class to check if the withdrawal will bring the balance below the minimum balance, and if so, print an error message and do not allow the withdrawal.
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


class SavingsAccount(BankAccount):
        minimum_balance=10000
        def withdraw(self,amount):
                self.amount=amount
                new_balance=self.balance - amount
                if new_balance<15000:
                    print("Error : Withdraw Not Allowed ")
                    print(f"Your Current Balance is : {self.balance}")
                    print(f"Minimum balance required is : {self.minimum_balance}")
                else:
                    print(f"Your New Balance after Withdraw is : {new_balance}")
                
name= input("Please Enter your Name : ")
person= BankAccount(name)
print(f"Welcome {person.name}")
print("Your Bank Details Are")
print()
print(f"Your Account Number is {person.Account_number}")
print(f"Your Account Balance is {person.balance}")
print(f"Your Account Interest Rate is {person.interest_rate}")

print('''Operation you want to perform : Deposite money / Withdraw Money 
DEPOSITE -- Press (1)
WITHDRAW -- Press (2)
CHECK INTEREST -- Press (3)''')
print()
user= int(input("Enter Your Choice : "))
if user ==1:
        amount=int(input("Please Enter the Amount for deposite : "))
        person.deposite(amount)
elif user ==2:
        amount=int(input("Please Enter the Amount for Withdraw : "))
        person.withdraw(amount)
elif user ==3:
        person.interest()
else:
        print("INVALID CHOICE ..................")
        
        

