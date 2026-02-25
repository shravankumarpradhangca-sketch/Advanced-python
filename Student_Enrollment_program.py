# Student Enrollment System
# students = {student_id: {"roll": int, "name": str}}
students = {}

# courses = {course_id: {"name": str, "limit": int}}
courses = {}

# enrollments = [(student_id, course_id)]
enrollments = []

# attendance = {(student_id, course_id): percentage}
attendance = {}

# grades = {(student_id, course_id): grade}
grades = {}


# ---------- Functions ----------
def add_student():
    sid = input("Enter Student ID: ")
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    students[sid] = {"roll": roll, "name": name}
    print("Student added successfully.\n")


def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    limit = int(input("Enter Course Limit: "))

    courses[cid] = {"name": cname, "limit": limit}
    print("Course added successfully.\n")


def enroll_student():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    if sid not in students or cid not in courses:
        print("Invalid Student or Course ID.\n")
        return

    count = sum(1 for s, c in enrollments if c == cid)
    if count >= courses[cid]["limit"]:
        print("Course limit reached.\n")
        return

    enrollments.append((sid, cid))
    attendance[(sid, cid)] = 0
    grades[(sid, cid)] = "NA"

    print("Student enrolled successfully.\n")


def mark_attendance():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    if (sid, cid) not in attendance:
        print("Student not enrolled in this course.\n")
        return

    att = float(input("Enter Attendance Percentage: "))
    attendance[(sid, cid)] = att

    if att < 75:
        print("⚠️ Attendance below 75% — Student is a defaulter!")
    print("Attendance updated.\n")


def assign_grade():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")

    if (sid, cid) not in grades:
        print("Enrollment not found.\n")
        return

    grade = input("Enter Grade (A/B/C/D/F): ")
    grades[(sid, cid)] = grade
    print("Grade assigned successfully.\n")


def student_report():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student not found.\n")
        return

    print("\n--- Student Report ---")
    print("Name:", students[sid]["name"])
    print("Roll No:", students[sid]["roll"])

    for (s, c) in enrollments:
        if s == sid:
            print("\nCourse:", courses[c]["name"])
            print("Attendance:", attendance[(s, c)], "%")
            print("Grade:", grades[(s, c)])

            if attendance[(s, c)] < 75:
                print("Status: Defaulter")
            else:
                print("Status: Regular")
    print()


def course_report():
    cid = input("Enter Course ID: ")

    if cid not in courses:
        print("Course not found.\n")
        return

    print("\n--- Course Wise Report ---")
    print("Course Name:", courses[cid]["name"])

    for (s, c) in enrollments:
        if c == cid:
            print("\nStudent:", students[s]["name"])
            print("Attendance:", attendance[(s, c)], "%")
            print("Grade:", grades[(s, c)])
    print()


# ---------- Menu ----------
while True:
    print("====== Student Enrollment System ======")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Mark Attendance")
    print("5. Assign Grade")
    print("6. Student Report")
    print("7. Course Wise Report")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        mark_attendance()
    elif choice == "5":
        assign_grade()
    elif choice == "6":
        student_report()
    elif choice == "7":
        course_report()
    elif choice == "8":
        print("Exiting system...")
        break
    else:
        print("Invalid choice.\n")



