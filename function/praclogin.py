def login():
    user1 = "Admin"
    pass1 = "Admin"
    try:
        username = input("Enter your username:")
        password = input("Enter your password:")
    
        if user1!= username:
            raise ZeroDivisionError
        elif pass1!=password:
            raise ValueError

    except ZeroDivisionError:
        print("username is invalid...")
        login()
    except ValueError:
        print("Password is invalid...")
        login()

    else:
        print("Login Succesfully")
        login()
    finally:
        print("Home")
login()
