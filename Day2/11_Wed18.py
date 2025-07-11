# Predefined username and password
correct_username = "admin"
correct_password = "1234"

# Take input from user
username = input("Enter username: ")

# Check username
if username == correct_username:
    password = input("Enter password: ")
    
    # Nested check for password
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
