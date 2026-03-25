# Dictionary to store account details
account = {}

# Function to create account
def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account created successfully!\n")


# Function to deposit money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount deposited!\n")


# Function to withdraw money
def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawal successful!\n")
    else:
        print("Insufficient balance!\n")


# Function to check balance
def check_balance():
    print("Name:", account["name"])
    print("Balance:", account["balance"], "\n")


# Main menu
def menu():
    while True:
        print("==== Bank System ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")

menu()