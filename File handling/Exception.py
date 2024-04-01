# exception -> an event that occurs to disrupt the normal flow of operation.

# try:
#     age=int(input("Enter age:\n"))
#     print(age)
# except:
#     print("Please enter numeric value")


# print("Xavier College")

# try:
#     a = int(input("Enter any number:\n"))
#     b = int(input("Enter any number:\n"))
#     c = a/b
# except ValueError:
#     print("Please provide numeric value")
# except ZeroDivisionError:
#     print("Zero will not divide any number")
# else:
#     print("The value of c is:",c)


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
except ValueError:
    print("Password is invalid...")

else:
    print("Login Succesfully")
finally:
    print("Home")