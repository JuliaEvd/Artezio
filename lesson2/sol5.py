login = input("Enter login")
password = input("Enter password")
right = {'Ivan': 'qwerty', 'Roma': 'zxcvbn', 'Rita': 'asdfgh', 'Masha': '123456'}
while password == right[login]:
    print("Password for user:", login, "is correct")
    break
else:
    print("Password for user:", login, "is incorrect")
    print("Please try again...")
    password = input("Enter password ")
