user=input("Enter username : ")

if user == "admin":
    print("Welcome,Pema")
    attendance = input("Enter attendance : ")
    if attendance =="Full":
        print("Staff attendance is full")
    elif attendance =="Half":
        prinnt("Staff attendance is half")
    elif attendance =="Morning":
        print("Staff attendance is Morning")
    else:
        print("Staff is absent")
else:
    print("Login Failed")        


