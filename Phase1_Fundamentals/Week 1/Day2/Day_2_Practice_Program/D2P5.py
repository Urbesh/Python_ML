#Use identity operators: Compare two lists using is and ==.
User_input=input("Enter List Elements Seperated by Space for list 1(string input only): ")
Sto=User_input.split()
User_input2=input("Enter List Elements Seperated by Space for list 2(string input only): ")
Sto2=User_input2.split()
print(Sto is Sto2)
if Sto==Sto2:
    print("(Sto is Sto2) returns False because x is not the same object as y, even if they have the same content")
else:
    print(" ")
if Sto==Sto2:
    print("True")
else:
    print("False")
print("To demonstrate the difference betweeen is and ==: this comparison returns True because Sto is equal to Sto2 and returns False because Sto is not equal to Sto2 ")