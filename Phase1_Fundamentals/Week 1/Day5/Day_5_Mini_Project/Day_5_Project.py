#Number Guessing Game 🎲
#Computer generates a random number (1–100).
#User keeps guessing until correct.
#After each guess → show "Too High", "Too Low", or "Correct".
#Count number of attempts.
import random
secret_number=random.randint(1, 100)
attempts=1
user_guess=int(input("Guess the number (1-100): "))
while user_guess!=secret_number:
    if user_guess<secret_number:
        print("Too Low")
    elif user_guess > secret_number:
        print("Too High")
    attempts+=1
    user_guess=int(input("Guess again: "))
print("Correct you guessed it in", attempts)