from functools import reduce

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
    Student("Vino", 102, "ECE", 60000),
    Student("Desigan", 103, "IT", 55000)
]

faculty = [
    Faculty("Nivetha", 201, 60000),
    Faculty("Dilli", 202, 25000),
    Faculty("Vineeth", 203, 40000)
]

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees Collected:", total_fees)
print("Total Salary of Faculty:", total_salary)