#College Result Management system and Teachers enter marks then calculate GPA.
class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.marks = {}
        self.gpa = 0

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def calculate_gpa(self):
        total_points = 0
        for mark in self.marks.values():
            if mark >= 90:
                gp = 10
            elif mark >= 80:
                gp = 9
            elif mark >= 70:
                gp = 8
            elif mark >= 60:
                gp = 7
            elif mark >= 50:
                gp = 6
            elif mark >= 40:
                gp = 5
            else:
                gp = 0
            total_points += gp

        if len(self.marks) > 0:
            self.gpa = total_points / len(self.marks)

    def display_result(self):
        print("\nStudent Roll:", self.roll)
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("GPA:", round(self.gpa, 2))


class ResultSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        student = Student(roll, name)
        self.students.append(student)

    def enter_marks(self):
        roll = int(input("Enter Roll No: "))
        for student in self.students:
            if student.roll == roll:
                n = int(input("Enter number of subjects: "))
                for i in range(n):
                    subject = input("Enter Subject Name: ")
                    marks = int(input("Enter Marks: "))
                    student.add_marks(subject, marks)

                student.calculate_gpa()
                print("Marks Added Successfully")
                return
        print("Student Not Found")

    def show_results(self):
        for student in self.students:
            student.display_result()


system = ResultSystem()

while True:
    print("\n1.Add Student")
    print("2.Enter Marks")
    print("3.Show Result")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        system.add_student()

    elif choice == 2:
        system.enter_marks()

    elif choice == 3:
        system.show_results()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")