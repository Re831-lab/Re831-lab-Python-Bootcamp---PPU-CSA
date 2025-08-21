username = input("Enter your username: ")
password = input("Enter your password: ")

username = username.lower()
username = username.replace(" ", "_")

password_length = len(password)

print("Fixed Username:", username)
print("Password Length:", password_length)

print(username == "admin")
print(password == "1234")
print(password_length >= 8)
print(username == "admin" and password == "1234")

print(f"Welcome {username}! Your password length is {password_length}.")
