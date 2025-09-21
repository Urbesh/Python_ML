#Update marks of a student by key
#Simple Version
A={
    "Muzan" : 20,
    "Akaza" : 80,
    "Doma" : 5,
    "Kokoshibo" : 70
}
print(f"The dictionary before update {A}")
A["Doma"]=10
print(f"The dictionary after update {A}")

#User Defined Version
a={}
n_keys=int(input("Enter the number of Student/Students: "))
for i in range(n_keys):
    keys=input(f"Enter Student Name {i+1}: ")
    values=int(input(f"Enter Marks Obrained by {keys}: "))
    a[keys]=values
print(f"Current Student dictionary: {a}")
while True:
    choise=input("Do you want to update marks obtained by a particular student (Y/N): ").lower()
    if choise=="y":
        Stu_name=input("Enter the Student's Name who's marks you want to update: ")
        if Stu_name in a:
            Stu_key=Stu_name
            Updated_marks=int(input(f"Enter the Updated Marks Obtained by {Stu_name}: "))
            a.update({Stu_key:Updated_marks})
            print(f"The Update Student dictionary: {a}")
        else:
            print("Student Doesn't Exists")
    elif choise=="n":
        break
    else:
        print("Invalid Input")