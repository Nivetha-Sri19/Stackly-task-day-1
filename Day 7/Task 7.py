class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Nivetha", 101, "CSE", 50000),
    Student("Dilli", 102, "ECE", 60000),
    Student("Vineeth", 103, "IT", 55000)
]

def get_name(s):
    return s.name

result = process_users(students, get_name)

print("Processed Result:")
print(result)