#Grade Calculator with Remarks: Input marks → print grade + remark (A = Excellent, B = Good, etc.).
marks = int(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 and 100.")
elif marks >= 90:
    grade = 'A'
    remark = 'Excellent'
elif marks >= 80:
    grade = 'B'
    remark = 'Good'
elif marks >= 70:
    grade = 'C'
    remark = 'Fair'
elif marks >= 60:
    grade = 'D'
    remark = 'Needs Improvement'
else:
    grade = 'F'
    remark = 'Fail'
print(f"Your grade is: {grade} - {remark}")