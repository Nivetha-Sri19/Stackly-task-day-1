class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

s1 = Student("Nivetha", 101, "CSE", 50000)
f1 = Faculty("Dilli", 201, 60000)
t1 = TempFaculty("Vino", 301, 40000, "6 months")

print(s1.name, s1.id, s1.dept, s1.fees)
print(f1.name, f1.id, f1.salary)
print(t1.name, t1.id, t1.salary, t1.duration)
