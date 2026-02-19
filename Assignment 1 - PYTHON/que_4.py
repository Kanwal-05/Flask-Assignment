def list_items():
    num = int(input("How Many Values You Want To Enter In A List : "))
    Final_list = []
    for i in range(num):
        user = input("Please Enter The Value : ")
        try:
            user = int(user) 
        except ValueError:
            pass               
    
        Final_list.append(user)
    print()
    print(f"Here Is The Final List : {Final_list}")


list_items()