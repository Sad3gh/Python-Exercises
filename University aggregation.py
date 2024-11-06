class Student:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"{self.name}"


class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def input_student(self):
        new_student = Student(input("Enter the name of the Student: "))
        self.add_student(new_student)

    def show_students(self):
        if not self.students:
            print("There is no student in university")
            return
        for index, student in enumerate(self.students, start=1):
            print(f"Student {index}: {student.show_info()}")

def main():

    my_university = University()
    while True:
        my_university.input_student()
        more = input("is there another student you want to add? (yes/no): ")
        if more.strip().lower() != 'yes':
            break

    my_university.show_students()

if __name__ == "__main__":
    main()