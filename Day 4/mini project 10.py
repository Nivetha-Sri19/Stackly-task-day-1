students = []

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")

    student = {
        "name": name,
        "courses": courses
    }

    students.append(student)
    print("Student added successfully!\n")

def update_courses():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == name:
            new_courses = input("Enter new courses (comma separated): ").split(",")
            student["courses"] = new_courses
            print("Courses updated!\n")
            return

    print("Student not found!\n")

def display_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\n===== Student Details =====")
    for student in students:
        print("Name:", student["name"])
        print("Courses:", ", ".join(student["courses"]))
    print()

def menu():
    while True:
        print("Course Enrollment System")
        print("1. Add Student")
        print("2. Update Courses")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_courses()
        elif choice == "3":
            display_students()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")

menu()