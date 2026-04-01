class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.login()
f.faculty_greet()

t = TempFaculty()
t.register()
t.login()
t.faculty_greet()
t.tempFaculty_greet()