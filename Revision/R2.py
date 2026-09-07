correct_username = "admin"
correct_password = "1234"

username = input("Enter your username:")
password  = input("Enter the password:")

if username == correct_username and password == correct_password:
    print("Login Successful")

elif username != correct_username:
    print("Wrong Username")

elif password != correct_password:
    print("Incorrect password")

