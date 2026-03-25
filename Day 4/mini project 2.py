def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total / 3

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

def print_report(student):
    print("\nREPORT CARD")
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])



def main():
    name = input("Enter student name: ")

    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))

    marks = [m1, m2, m3]

    total = calculate_total(marks)
    average = calculate_average(total)
    grade = get_grade(average)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    print_report(student)

main()