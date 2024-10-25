display_student_grades = []

while True:
    student_grade = int(input("Enter Grade: "))
    
    if student_grade >= 90:
        print(f"A = {student_grade}")
        display_student_grades.append(student_grade)
    elif student_grade >= 75:
        print(f"B = {student_grade}")
        display_student_grades.append(student_grade)
    elif student_grade >= 60:
        print(f"C = {student_grade}")
        display_student_grades.append(student_grade)
    elif student_grade < 60:
            print("F")
            display_student_grades.append(student_grade)
    else:
        print("Must Enter Valid Number")
   
    user_input = input("Do you wish to contine? (y/n: )")
    if user_input.lower() != 'y':
        user_input = True
        break

# displays list of student grades 
def view_student_grades():
    print(display_student_grades)

view_student_grades()

avg = sum(display_student_grades) / len(display_student_grades)
print(f"The avg is: {avg}")

