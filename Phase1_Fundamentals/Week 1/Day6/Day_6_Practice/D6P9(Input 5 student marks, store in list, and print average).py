#Input 5 student marks, store in list, and print average.
a=input("Enter the list elements followed by a space: ").split()
a=[int(x) for x in a]
print("Student Marks is:",a)
Total_sum=sum(a)
count=len(a)
if count>0:
    average=Total_sum/count
    print("The average is: ",average)
else:
    print("Cannot Calculate average of an empty list")