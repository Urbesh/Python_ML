#Store student names and marks in two lists.
#Features:
#Add a new student.
#Update marks.
#Display all students.
#Find topper (highest marks).
student_list=input("Enter Student's Names followed by a space: ").split()
student_marks=[]
for i in student_list:
    marks=int(input(f"Enter the marks obtained by {i}: "))
    student_marks.append(marks)
while True:
    print("Actions that can be performed\n1. Add a new student\n2. Update marks\n3. Display all students\n4. Find topper\n5. Exit")
    choise=int(input("Enter the action you want to perform: "))
    if choise==1:
        add_students=input("Enter Student/Student's name followed by a space: ").split()
        for j in add_students:
            student_list.append(j)
            new_student_marks=int(input(f"Enter the marks obtained by {j}: "))
            student_marks.append(new_student_marks)
    elif choise==2:
        update_marks=input("Enter student name who's marks you want to update: ")
        if update_marks in student_list:
            student_index=student_list.index(update_marks)
            student_marks[student_index]=int(input("Enter the updated marks: "))
        else:
            print("Student Doesn't Exists")
    elif choise==3:
        print(f"Name of the Students: {student_list}\nAnd respective marks obtained by them: {student_marks}")
    elif choise==4:
        hightest_marks=max(student_marks)
        hightest_scorer_index=student_marks.index(hightest_marks)
        highest_scorer=student_list[hightest_scorer_index]
        print(f"The Highest Score is {hightest_marks} and it is obtained by {highest_scorer}")
    elif choise==5:
        break
    else:
        print("Invalid Input")