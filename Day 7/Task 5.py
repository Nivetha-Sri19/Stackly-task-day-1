class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

students = [
    Student("Nivetha", 101, "CSE", 50000),
    Student("Dilli", 102, "ECE", 60000),
    Student("Vineeth", 103, "IT", 55000)
]

high_fee_students = list(filter(lambda s: s.fees > 50000, students))

print("Students with fees > 50000:")
for s in high_fee_students:
    print(s.name, s.fees)

faculty = [
    Faculty("Vino", 201, 60000),
    Faculty("Subha", 202, 25000),
    Faculty("Latha", 203, 40000)
]

high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f.name, f.salary)