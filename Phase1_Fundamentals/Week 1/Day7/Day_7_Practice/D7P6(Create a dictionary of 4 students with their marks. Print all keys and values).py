#Create a dictionary of 4 students with their marks. Print all keys and values.
Stu_name_marks={
    "Muzan" : "20",
    "Doma" : "05",
    "Akaza" : "80",
    "Kokoshibo" : "70"
}
print(Stu_name_marks)

#User Defined Version
stu_data={}
n_keys=int(input("Enter the number of Student/Students: "))
for i in range(n_keys):
    keys=input(f"Enter the Student Name {i+1}: ")
    values=int(input(f"Enter marks obtained by {keys}: "))
    stu_data[keys]=values
print("The result is:")
print(stu_data)