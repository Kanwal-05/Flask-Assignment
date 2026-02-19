# Create a function to calculate the sum of the first n positive integers. 
def sum(num):
    return num * (num + 1) // 2

num= int(input("Enter the number to calculate the sum of the first n positive integers : "))
print(sum(num))