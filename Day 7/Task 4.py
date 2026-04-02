class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

students = [
    Student("Nivetha", 101, "CSE", 50000),
    Student("Vineeth", 102, "ECE", 40000),
    Student("Dilli", 103, "IT", 45000)
]

names = list(map(lambda s: s.name, students))

print("Student Names:")
print(names)