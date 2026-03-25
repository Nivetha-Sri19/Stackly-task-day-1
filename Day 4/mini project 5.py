visitors = set()

def add_visitor():
    name = input("Enter visitor name: ")
    
    if name in visitors:
        print("Visitor already counted!\n")
    else:
        visitors.add(name)
        print("Visitor added!\n")

def show_visitors():
    print("Unique Visitors:", visitors)
    print("Total Unique Visitors:", len(visitors), "\n")

def menu():
    while True:
        print("Visitor Counter")
        print("1. Add Visitor")
        print("2. Show Visitors")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_visitor()
        elif choice == "2":
            show_visitors()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")

menu()