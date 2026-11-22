
# ==========================================
# STUDENT GRADE MANAGER
# ==========================================

students = []


# 1. GET GRADE FUNCTION
def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# 2. ADD STUDENT FUNCTION
def add_student():

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    try:
        mark = float(input("Enter student mark: "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100!")
            return

        grade = get_grade(mark)

        student = {
            "name": name,
            "mark": mark,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid number!")


# 3. SHOW RESULTS FUNCTION
def show_results():

    if len(students) == 0:
        print("No student records found!")
        return

    print("\nName        Mark   Grade")

    for student in students:
        print(
            f"{student['name']:<12}"
            f"{student['mark']:<7.0f}"
            f"{student['grade']}"
        )

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(
        f"\nAverage: {average:.1f}"
        f"   Highest: {highest:.0f}"
        f"   Lowest: {lowest:.0f}"
    )


# 4. MAIN MENU
while True:

    print("\n==============================")
    print("    STUDENT GRADE MANAGER")
    print("==============================")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        show_results()

    elif choice == "3":

        print("Thank you! Program closed.")
        break

    else:

        print("Invalid choice! Try again.")
# My first GitHub update
