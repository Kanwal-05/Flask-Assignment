def Create_dict():
    num = int(input("How Many Elements You Want To Enter In A Dictionary : "))
    dictionary={}
    for i in range(num):
        a=input("Please Enter the Key : ")
        b=input("Please Enter the Value : ")
        print()
        try:
            a = int(a) 
        except ValueError:
            pass 

        try:
            b = int(b) 
        except ValueError:
            pass 
        dictionary.update({a:b})
    print(f"Dictionary is {dictionary}")
    print()
    print(f"Values is {dictionary.values()}")

Create_dict()
