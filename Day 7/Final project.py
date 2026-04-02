from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return "Student: " + self.name + " " + str(self.id) + " " + self.dept + " " + str(self.fees)

class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return "Faculty: " + self.name + " " + str(self.id) + " " + str(self.salary)

def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Latha", 101, "CSE", 50000),
    Student("Vino", 102, "ECE", 60000),
    Student("Subha", 103, "IT", 55000)
]

faculty = [
    Faculty("Nivetha", 201, 60000),
    Faculty("Dilli", 202, 25000),
    Faculty("Vineeth", 203, 40000)
]


print("All Details:")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\nSorted Students (by fees):")
for s in students:
    print(s.name, s.fees)

print("\nSorted Faculty (by salary):")
for f in faculty:
    print(f.name, f.salary)

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nFiltered Students (fees > 50000):")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nFiltered Faculty (salary > 30000):")
for f in high_salary_faculty:
    print(f.name, f.salary)

student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)


def get_name(user):
    return user.name
processed_names = process_users(students, get_name)
print("\nProcessed Names:", processed_names)
combined = reduce(
    lambda acc, s: acc + s,
    map(lambda s: s.fees, filter(lambda s: s.fees > 50000, students)),
    0
)

print("\nTotal fees of high paying students:", combined)