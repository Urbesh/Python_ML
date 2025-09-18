#Simple Quiz App
#Ask 3 MCQ questions.
#Keep score based on correct answers.
#Use if-elif to check.
score = 0
print("Welcome to the Quiz! Answer the following questions:")
q1=input("1. What is the capital of France?\n a) Berlin\n b) Madrid\n c) Paris\nYour answer: ")
if q1.lower()=='c':
    score += 1
q2=input("2. What is 2 + 2?\n a) 3\n b) 4\n c) 5\nYour answer: ")
if q2.lower()=='b':
    score += 1
q3=input("3. Which planet is known as the Red Planet?\n a) Earth\n b) Mars\n c) Jupiter\nYour answer: ")
if q3.lower()=='b':
    score += 1
print(f"Your total score is: {score}/3")