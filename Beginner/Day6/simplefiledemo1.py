students = []

filepath = "./datastore/students.txt"


def print_students_titlecase():
    for student in students:
        stud = {"roll_number": student['roll_number'],
                "name": student['name'], "student_age": student['student_age']}
        print(stud)


def save_file(student):
    try:
        f = open(filepath, "a")
        f.write(
            f'{student["roll_number"]} {student["name"]} {student["student_age"]}\n')
        f.close()

        student = {"roll_number": student["roll_number"],
                   "name": student["name"], "student_age": student["student_age"]}
        students.append(student)
    except Exception as error:
        print("Could not save file ", error)


def read_file():
    try:
        f = open(filepath, "r")

        for student in f.readlines():
            values = student.split()
            # add_student(values[0], values[1], values[2])

        f.close()
    except Exception:
        print("Could not read file")


# -------------------------------------------
read_file()
print_students_titlecase()

roll_number = input("Enter student ID: ")
student_name = input("Enter student name: ")
student_age = input("Enter student age: ")

# student = add_student(student_name, roll_number, student_age)
student = {"roll_number": roll_number, "name": student_name, "student_age": student_age}

save_file(student)
