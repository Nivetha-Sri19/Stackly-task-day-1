from abc import ABC, abstractmethod

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
        return "Student: " + self.name + ", " + str(self.id) + ", " + self.dept + ", " + str(self.fees)

class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return "Faculty: " + self.name + ", " + str(self.id) + ", Salary: " + str(self.salary)

class TempFaculty(AbstractUser):
    def __init__(self, name, id, salary, duration):
        self.name = name
        self.id = id
        self.salary = salary
        self.duration = duration

    def get_details(self):
        return "TempFaculty: " + self.name + ", " + str(self.id) + ", " + str(self.salary) + ", " + self.duration

s1 = Student("Rahul", 101, "CSE", 50000)
f1 = Faculty("Meena", 201, 60000)
t1 = TempFaculty("Arun", 301, 40000, "6 months")

print(s1.get_details())
print(f1.get_details())
print(t1.get_details())