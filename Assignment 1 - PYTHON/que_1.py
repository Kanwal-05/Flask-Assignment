# Create a function to find whether a given number (accept from the user) is even or odd, 
# print out an appropriate message to the user. 
def is_odd_even(n):
    if n%2==0:
        print(f"The Number {n} is Even Number")
        print("Thankyou....")
    else:
        print(f"The Number {n} is ODD Number")
        print("Thankyou....")


n=int(input("Enter the number you want to check weither it is EVEN or ODD : "))
is_odd_even(n)
