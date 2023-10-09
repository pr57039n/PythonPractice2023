username = input("What is your desired username? \n")
password = input("What is your desired password? \n")
password_length = len(password)
password_hidden = ('*' * password_length)

print(f"Hello {username} your password {password_hidden} is {password_length} characters long")