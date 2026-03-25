employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("Employee added successfully!\n")

def display_employees():
    if len(employees) == 0:
        print("No employees found.\n")
        return

    print("\nEmployee List:")
    for i, emp in enumerate(employees):
        print(f"{i + 1}. Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")
    print()

def update_employee():
    display_employees()
    index = int(input("Enter employee number to update: ")) - 1

    if 0 <= index < len(employees):
        emp = employees[index]

        emp["name"] = input("Enter new name: ")
        emp["age"] = int(input("Enter new age: "))
        emp["role"] = input("Enter new role: ")
        emp["salary"] = float(input("Enter new salary: "))

        print("Employee updated successfully!\n")
    else:
        print("Invalid employee number!\n")


def delete_employee():
    display_employees()
    index = int(input("Enter employee number to delete: ")) - 1

    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee deleted successfully!\n")
    else:
        print("Invalid employee number!\n")


def menu():
    while True:
        print("Employee Management System ")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()