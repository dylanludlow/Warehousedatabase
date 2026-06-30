students = {}
teachers = {}
homeroom_teachers = {}

print("School Management System")

while True:
    print("\nAvailable commands:")
    print("create")
    print("manage")
    print("end")

    command = input("Enter command: ").lower()

    if command == "create":

        while True:
            print("\nCreate Menu:")
            print("student")
            print("teacher")
            print("homeroom teacher")
            print("end")

            choice = input("Choose user type: ").lower()

            if choice == "student":
                first = input("First name: ")
                last = input("Last name: ")
                class_name = input("Class: ")

                full_name = first + " " + last

                if full_name not in students:
                    students[full_name] = []

                students[full_name].append(class_name)

                print("Student created.")

            elif choice == "teacher":
                first = input("First name: ")
                last = input("Last name: ")
                subject = input("Subject: ")

                classes = []

                print("Enter classes taught (blank line to finish):")
                while True:
                    class_name = input("Class: ")
                    if class_name == "":
                        break
                    classes.append(class_name)

                full_name = first + " " + last

                teachers[full_name] = {
                    "subject": subject,
                    "classes": classes
                }

                print("Teacher created.")

            elif choice == "homeroom teacher":
                first = input("First name: ")
                last = input("Last name: ")
                class_name = input("Class they lead: ")

                full_name = first + " " + last

                homeroom_teachers[full_name] = class_name

                print("Homeroom teacher created.")

            elif choice == "end":
                break

            else:
                print("Invalid option.")

    elif command == "manage":

        while True:
            print("\nManage Menu:")
            print("class")
            print("student")
            print("teacher")
            print("homeroom teacher")
            print("end")

            choice = input("Choose option: ").lower()

            if choice == "class":
                class_name = input("Enter class: ")

                print("\nStudents:")
                found = False

                for student, classes in students.items():
                    if class_name in classes:
                        print(student)
                        found = True

                if not found:
                    print("No students found.")

                print("\nHomeroom Teacher:")
                teacher_found = False

                for teacher, teacher_class in homeroom_teachers.items():
                    if teacher_class == class_name:
                        print(teacher)
                        teacher_found = True

                if not teacher_found:
                    print("No homeroom teacher assigned.")

            elif choice == "student":
                full_name = input("Enter student's first and last name: ")

                if full_name not in students:
                    print("Student not found.")
                else:
                    print("Classes:")
                    for class_name in students[full_name]:
                        print(class_name)

                    print("\nTeachers:")
                    for teacher, info in teachers.items():
                        for class_name in students[full_name]:
                            if class_name in info["classes"]:
                                print(teacher, "-", info["subject"])

            elif choice == "teacher":
                full_name = input("Enter teacher's first and last name: ")

                if full_name not in teachers:
                    print("Teacher not found.")
                else:
                    print("Classes taught:")
                    for class_name in teachers[full_name]["classes"]:
                        print(class_name)

            elif choice == "homeroom teacher":
                full_name = input("Enter homeroom teacher's first and last name: ")

                if full_name not in homeroom_teachers:
                    print("Homeroom teacher not found.")
                else:
                    class_name = homeroom_teachers[full_name]

                    print("Students:")
                    found = False

                    for student, classes in students.items():
                        if class_name in classes:
                            print(student)
                            found = True

                    if not found:
                        print("No students in this class.")

            elif choice == "end":
                break

            else:
                print("Invalid option.")

    elif command == "end":
        print("Program ended.")
        break

    else:
        print("Invalid command.")