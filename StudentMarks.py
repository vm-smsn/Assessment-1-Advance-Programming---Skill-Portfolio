'''
Vince Michael J. Samson
ID: 04-24-0147
10/6/2025 - Oct.11,2026
Advance Programming: Excercise 3 - Students Manager
'''

def load_students():
    students = []
    try:
        with open("studentMarks.txt", "r") as file:
            num_students = int(file.readline().strip())
            for i in range(num_students):
                data = file.readline().strip().split(',')
                student = {
                    'id': data[0],
                    'name': data[1],
                    'marks': [int(data[2]), int(data[3]), int(data[4])],
                    'exam': int(data[5])
                }
                students.append(student)
        print(f"Loaded {len(students)} students")
    except:
        print("Error loading file")
    return students

def calc_percentage(student):
    coursework_total = sum(student['marks'])
    total_marks = coursework_total + student['exam']
    return (total_marks / 160) * 100

def get_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def disp_student(student):
    percentage = calc_percentage(student)
    grade = get_grade(percentage)
    
    print(f"\nName: {student['name']}")
    print(f"ID: {student['id']}")
    print(f"Coursework: {sum(student['marks'])}/60")
    print(f"Exam: {student['exam']}/100")
    print(f"Overall: {percentage:.1f}%")
    print(f"Grade: {grade}")

def view_all_students(students):
    print("\n--- ALL STUDENT RECORDS ---")
    
    total_percentage = 0
    for student in students:
        disp_student(student)
        total_percentage += calc_percentage(student)
        print("-------------------")
    
    if students:
        average = total_percentage / len(students)
        print(f"\nTotal students: {len(students)}")
        print(f"Average percentage: {average:.1f}%")

def view_single_student(students):
    print("\n--- VIEW INDIVIDUAL STUDENT ---")
    
    # Show student list
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} ({student['id']})")
    
    try:
        choice = int(input("\nEnter student number: ")) - 1
        if 0 <= choice < len(students):
            disp_student(students[choice])
        else:
            print("Invalid choice!")
    except:
        print("Please enter a valid number!")

def show_highest_student(students):
    if not students:
        print("No students found!")
        return
    
    highest = students[0]
    for student in students:
        if calc_percentage(student) > calc_percentage(highest):
            highest = student
    
    print("\n HIGHEST SCORING STUDENT ")
    disp_student(highest)

def show_lowest_student(students):
    if not students:
        print("No students found!")
        return
    
    lowest = students[0]
    for student in students:
        if calc_percentage(student) < calc_percentage(lowest):
            lowest = student
    
    print("\n LOWEST SCORING STUDENT ")
    disp_student(lowest)

def main():
    students = load_students()
    
    while True:
        print("\n STUDENT MARKS SYSTEM ")
        print("1. View all students")
        print("2. View individual student")
        print("3. Show highest scoring student")
        print("4. Show lowest scoring student")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            view_all_students(students)
        elif choice == '2':
            view_single_student(students)
        elif choice == '3':
            show_highest_student(students)
        elif choice == '4':
            show_lowest_student(students)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()