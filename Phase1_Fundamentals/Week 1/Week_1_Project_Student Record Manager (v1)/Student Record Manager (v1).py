#🎯 Goal
#Build a small console-based system to manage student records (names, grades, subjects).
#✅ Features to Implement
#Add a Student Record
#Input name, roll no, subjects, marks.
#Store them in a dictionary or list of tuples.
#View All Students
#Display all stored records neatly.
#Search a Student by Roll No
#Use conditionals & loops to find and display record.
#Calculate Average Marks
#Use loops and functions.
#Find Topper
#Return student with highest marks.
#Subjects Chosen by particular student.
#Collect all subjects across students → print unique subjects using a set
students_list=[]
student_subject_list=[]

print("===== Student Record Manager =====")
while True:
    print("1. Add Student\n2. View All Students\n3. Search Student\n4. Calculate Average\n5. Find Topper\n6. Subjects Chosen by Particular Student\n7. Exit")
    user_choise=int(input("Choose Option: "))
    if user_choise==1:
        student_num=int(input("Enter Number of Students You Want to Enter: "))
        for i in range(student_num):
            marks=[]
            student_name=input(f"Enter Name of Student {i+1}: ")
            student_roll=int(input(f"Enter Roll Number of {student_name}: "))
            student_subject=input(f"Enter the Subjects taken by {student_name} separated by a space: ").split()
            for j in student_subject:
                student_marks=int(input(f"Enter the Marks obtained by {student_name} in {j}: "))
                marks.append(student_marks)
                total_marks=sum(marks)
            subject={"Name":student_name, "Subjects":student_subject,"Respective_Marks":marks}
            student_subject_list.append(subject)
            student={"Name":student_name, "Roll":student_roll, "Total Marks":total_marks}
            students_list.append(student)
    elif user_choise==2:
        print("Student Records:")
        for s in students_list:
            print(f"Roll: {s['Roll']} | Name: {s['Name']:<10} | Total Marks: {s['Total Marks']}")
    elif user_choise == 3:
        find_student = input("Enter The Student's name you are searching: ")
        for s in students_list:
            if s["Name"].lower()==find_student.lower():  
                print("Student Found!\nStudent details:")
                print(f"Roll: {s['Roll']} | Name: {s['Name']:<10}")
                break
        else:
            print("Student not found!")
    elif user_choise==4:
        Stu_input=input("Enter the Student's Name who's average marks you want to calculate: ")
        n_subjects=len(student_subject)
        for s in students_list:
            average=s['Total Marks']/n_subjects
            if s["Name"].lower()==Stu_input.lower():
                print(f"Marks scored by {s['Name']} out of {n_subjects*100} is: {s['Total Marks']}\n So average marks scored by {Stu_input} in every subject is: {average}")
        else:
            print("Student not found!")
    elif user_choise==5:
        if not students_list:
            print("No students available yet.")
        else:
            highest_marks = max(s["Total Marks"] for s in students_list)
            toppers = [s for s in students_list if s["Total Marks"] == highest_marks]
            print(f"Highest Marks: {highest_marks}")
        for t in toppers:
            print(f" - {t['Name']} (Roll: {t['Roll']})")
    elif user_choise==6:
        Stu_sub=input("Enter the Student's Name to see what subjects they have chosen: ")
        for s in student_subject_list:
            if s["Name"].lower()==Stu_sub.lower():
                print(f"The Subjects Chosen by {Stu_sub} are:\n {s['Subjects']}")
        else:
            print("Student not found!")
    elif user_choise==7:
        break
    else:
        print("Invalid Input")