# This are Error not Exceptions:
# 1. Syntax Errors
# 2. Indentation errors
# 3. Tab error
# All errors apart from above two can be handeld and managed through exception 
# List of all exception is on python's official website


# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))

# try:
#     c=a/b
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception as err: #to handl eall exceptions at once
#     print(f"ohh Shit!! we got the error {err}")
# else:
#     print("Hurrayyy!! there is no exceptions")
# finally:
#     print("I don't care about your code I will run always!!") 
# print('Division done')

# age=int(input("Enter your age: "))
# try:
#     if age<10 or age>18:
#         raise ValueError("Your age should be between 10 and 18")
#     else:
#         print("Welcome to the club")
# except Exception as err:
#     print(f"Oopss!! An error  occured called {err}")
# print("We will start Soon!!!")