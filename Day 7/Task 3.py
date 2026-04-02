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
    Student("Arjun", 101, "CSE", 50000),
    Student("Vino", 102, "ECE", 40000),
    Student("Subbu", 103, "IT", 45000)
]

students.sort(key=lambda x: x.fees)

print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)

faculty = [
    Faculty("Nivetha", 201, 60000),
    Faculty("Dilli", 202, 55000),
    Faculty("Vineeth", 203, 65000)
]

faculty.sort(key=lambda x: x.salary)

print("\nFaculty sorted by salary:")
for f in faculty:
    print(f.name, f.salary)