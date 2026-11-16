import mysql.connector


# =========================================================
# 1. ADD STUDENT
# =========================================================

def add_student():

    print("\n========== ADD STUDENT ==========")

    student_name = input("Enter student name: ")

    mathematics = int(input("Enter Mathematics marks: "))
    statistics = int(input("Enter Statistics marks: "))
    computer_science = int(input("Enter Computer Science marks: "))
    english = int(input("Enter English marks: "))
    hr_ethics = int(input("Enter Human Resources & Ethics marks: "))

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (
            student_name,
            mathematics,
            statistics,
            computer_science,
            english,
            hr_ethics
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        student_name,
        mathematics,
        statistics,
        computer_science,
        english,
        hr_ethics
    ))

    connection.commit()

    print("\nStudent Added Successfully")

    cursor.close()
    connection.close()


# =========================================================
# 2. VIEW STUDENTS
# =========================================================

def view_students():

    print("\n========== ALL STUDENTS ==========")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:

        print("No students found.")

    else:

        for student in students:

            print("\n========================================")
            print("Student ID              :", student[0])
            print("Student Name            :", student[1])
            print("Mathematics             :", student[2])
            print("Statistics              :", student[3])
            print("Computer Science        :", student[4])
            print("English                 :", student[5])
            print("Human Resources & Ethics:", student[6])
            print("========================================")

    cursor.close()
    connection.close()


# =========================================================
# 3. SEARCH STUDENT
# =========================================================

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    print("1. Search by Student ID")
    print("2. Search by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:

            print("Student not found.")

        else:

            print("\n========================================")
            print("Student ID              :", student[0])
            print("Student Name            :", student[1])
            print("Mathematics             :", student[2])
            print("Statistics              :", student[3])
            print("Computer Science        :", student[4])
            print("English                 :", student[5])
            print("Human Resources & Ethics:", student[6])
            print("========================================")

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        students = cursor.fetchall()

        if len(students) == 0:

            print("Student not found.")

        else:

            for student in students:

                print("\n========================================")
                print("Student ID              :", student[0])
                print("Student Name            :", student[1])
                print("Mathematics             :", student[2])
                print("Statistics              :", student[3])
                print("Computer Science        :", student[4])
                print("English                 :", student[5])
                print("Human Resources & Ethics:", student[6])
                print("========================================")

    else:

        print("Invalid choice.")

    cursor.close()
    connection.close()


# =========================================================
# 4. UPDATE STUDENT
# =========================================================

def update_student():

    print("\n========== UPDATE STUDENT ==========")

    print("1. Update by Student ID")
    print("2. Update by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        student = cursor.fetchone()

    else:

        print("Invalid choice.")

        cursor.close()
        connection.close()

        return

    if student is None:

        print("Student not found.")

        cursor.close()
        connection.close()

        return

    print("\nStudent found.")
    print("Student ID   :", student[0])
    print("Student Name :", student[1])

    new_name = input("Enter new student name: ")

    new_mathematics = int(
        input("Enter new Mathematics marks: ")
    )

    new_statistics = int(
        input("Enter new Statistics marks: ")
    )

    new_computer_science = int(
        input("Enter new Computer Science marks: ")
    )

    new_english = int(
        input("Enter new English marks: ")
    )

    new_hr_ethics = int(
        input("Enter new Human Resources & Ethics marks: ")
    )

    cursor.execute("""
        UPDATE students
        SET
            student_name=%s,
            mathematics=%s,
            statistics=%s,
            computer_science=%s,
            english=%s,
            hr_ethics=%s
        WHERE student_id=%s
    """, (
        new_name,
        new_mathematics,
        new_statistics,
        new_computer_science,
        new_english,
        new_hr_ethics,
        student[0]
    ))

    connection.commit()

    print("\nStudent details updated successfully.")

    cursor.close()
    connection.close()


# =========================================================
# 5. DELETE STUDENT
# =========================================================

def delete_student():

    print("\n========== DELETE STUDENT ==========")

    print("1. Delete by Student ID")
    print("2. Delete by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        student = cursor.fetchone()

    else:

        print("Invalid choice.")

        cursor.close()
        connection.close()

        return

    if student is None:

        print("Student not found.")

        cursor.close()
        connection.close()

        return

    print("\nStudent found.")
    print("Student ID   :", student[0])
    print("Student Name :", student[1])

    confirm = input(
        "Are you sure you want to delete this student? (yes/no): "
    )

    if confirm.lower() == "yes":

        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student[0],)
        )

        connection.commit()

        print("\nStudent deleted successfully.")

    else:

        print("\nDelete operation cancelled.")

    cursor.close()
    connection.close()


# =========================================================
# 6. CALCULATE TOTAL MARKS
# =========================================================

def calculate_total():

    print("\n========== CALCULATE TOTAL MARKS ==========")

    print("1. Search by Student ID")
    print("2. Search by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        student = cursor.fetchone()

    else:

        print("Invalid choice.")

        cursor.close()
        connection.close()

        return

    if student is None:

        print("Student not found.")

    else:

        total = (
            student[2]
            + student[3]
            + student[4]
            + student[5]
            + student[6]
        )

        print("\n========================================")
        print("Student ID   :", student[0])
        print("Student Name :", student[1])
        print("Total Marks  :", total, "/ 500")
        print("========================================")

    cursor.close()
    connection.close()


# =========================================================
# 7. CALCULATE PERCENTAGE
# =========================================================

def calculate_percentage():

    print("\n========== CALCULATE PERCENTAGE ==========")

    print("1. Search by Student ID")
    print("2. Search by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        student = cursor.fetchone()

    else:

        print("Invalid choice.")

        cursor.close()
        connection.close()

        return

    if student is None:

        print("Student not found.")

    else:

        total = (
            student[2]
            + student[3]
            + student[4]
            + student[5]
            + student[6]
        )

        percentage = (total / 500) * 100

        print("\n========================================")
        print("Student ID   :", student[0])
        print("Student Name :", student[1])
        print("Total Marks  :", total, "/ 500")
        print("Percentage   :", percentage, "%")
        print("========================================")

    cursor.close()
    connection.close()


# =========================================================
# TEST CURRENT STEP
# =========================================================

calculate_percentage()

# =========================================================
# 8. GENERATE GRADE
# =========================================================

def generate_grade():

    print("\n========== GENERATE GRADE ==========")

    print("1. Search by Student ID")
    print("2. Search by Student Name")

    choice = input("Enter your choice: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    if choice == "1":

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )

        student = cursor.fetchone()

    elif choice == "2":

        student_name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_name=%s",
            (student_name,)
        )

        student = cursor.fetchone()

    else:

        print("Invalid choice.")

        cursor.close()
        connection.close()

        return

    if student is None:

        print("Student not found.")

    else:

        total = (
            student[2]
            + student[3]
            + student[4]
            + student[5]
            + student[6]
        )

        percentage = (total / 500) * 100

        if percentage >= 90:
            grade = "A+"

        elif percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        else:
            grade = "F"

        print("\n========================================")
        print("Student ID   :", student[0])
        print("Student Name :", student[1])
        print("Total Marks  :", total, "/ 500")
        print("Percentage   :", percentage, "%")
        print("Grade        :", grade)
        print("========================================")

    cursor.close()
    connection.close()


generate_grade()

# =========================================================
# 9. DISPLAY TOPPER
# =========================================================

def display_topper():

    print("\n========== DISPLAY TOPPER ==========")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            student_id,
            student_name,
            mathematics,
            statistics,
            computer_science,
            english,
            hr_ethics
        FROM students
    """)

    students = cursor.fetchall()

    if len(students) == 0:

        print("No students found.")

    else:

        topper = students[0]

        topper_total = (
            topper[2]
            + topper[3]
            + topper[4]
            + topper[5]
            + topper[6]
        )

        for student in students:

            total = (
                student[2]
                + student[3]
                + student[4]
                + student[5]
                + student[6]
            )

            if total > topper_total:

                topper = student
                topper_total = total

        topper_percentage = (topper_total / 500) * 100

        print("\n========================================")
        print("              TOPPER DETAILS")
        print("========================================")
        print("Student ID   :", topper[0])
        print("Student Name :", topper[1])
        print("Total Marks  :", topper_total, "/ 500")
        print("Percentage   :", topper_percentage, "%")
        print("========================================")

    cursor.close()
    connection.close()


display_topper()

# =========================================================
# 10. FAILED AND QUALIFIED STUDENTS
# =========================================================

def failed_qualified_students():

    print("\n========== FAILED & QUALIFIED STUDENTS ==========")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="intel@i5",
        database="student_management"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:

        print("No students found.")

    else:

        total_students = len(students)

        qualified_count = 0
        failed_count = 0

        for student in students:

            total = (
                student[2]
                + student[3]
                + student[4]
                + student[5]
                + student[6]
            )

            percentage = (total / 500) * 100

            if percentage >= 40:

                qualified_count = qualified_count + 1

            else:

                failed_count = failed_count + 1

        qualified_percentage = (
            qualified_count / total_students
        ) * 100

        failed_percentage = (
            failed_count / total_students
        ) * 100

        print("\n========================================")
        print("Total Students       :", total_students)
        print("Qualified Students   :", qualified_count)
        print("Failed Students      :", failed_count)
        print("Qualified Percentage :", qualified_percentage, "%")
        print("Failed Percentage    :", failed_percentage, "%")
        print("========================================")

    cursor.close()
    connection.close()


# =========================================================
# 11. MAIN MENU
# =========================================================

def main_menu():

    while True:

        print("\n==============================================")
        print("        STUDENT MANAGEMENT SYSTEM")
        print("==============================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Total Marks")
        print("7. Calculate Percentage")
        print("8. Generate Grade")
        print("9. Display Topper")
        print("10. Failed & Qualified Students")
        print("11. Exit")

        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            calculate_total()

        elif choice == "7":

            calculate_percentage()

        elif choice == "8":

            generate_grade()

        elif choice == "9":

            display_topper()

        elif choice == "10":

            failed_qualified_students()

        elif choice == "11":

            print("\nThank you for using Student Management System.")
            print("Program exited successfully.")

            break

        else:

            print("\nInvalid choice. Please enter a number from 1 to 11.")


# =========================================================
# START PROGRAM
# =========================================================

main_menu()