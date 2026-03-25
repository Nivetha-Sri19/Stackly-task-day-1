users = {
    "admin": "Nivetha",
    "user1": "Nivetha@2001",
    "Nivetha": "12345678"
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        if users[username] == password:
            print("Login Successful!")
        else:
            print("Wrong Password!")
    else:
        print("User not found!")

login()