# ---------------------------------------------
# College Result Management System (Intermediate)
# ---------------------------------------------

students = []   # List to store all student records


# Function to calculate grade
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"


# Function to add a new student
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")

    print("Enter marks out of 100:")
    m1 = float(input("Maths: "))
    m2 = float(input("Physics: "))
    m3 = float(input("Chemistry: "))
    m4 = float(input("English: "))
    m5 = float(input("Computer: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100
    grade = get_grade(percentage)

    record = {
        "name": name,
        "Maths": m1,
        "Physics": m2,
        "Chemistry": m3,
        "English": m4,
        "Computer": m5,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    students.append(record)
    print("Student added successfully!\n")


# Function to display all students
def display_all():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n--- All Student Records ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']}  |  {s['Percentage']}%  | Grade: {s['Grade']}")
    print()


# Function to view a specific student's full result
def view_student():
    name = input("\nEnter student name to view result: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("\n--- Student Result ---")
            for key, value in s.items():
                print(f"{key}: {value}")
            print()
            return

    print("Student not found!\n")


# Main menu loop
while True:
    print("==== College Result System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Single Student Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        view_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
