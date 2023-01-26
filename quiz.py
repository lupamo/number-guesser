import random
from random import randint


picked_number = randint(1, 15)
print("The computer has picked a random number for you.")
print("Clue: It is between 1 and 15 (both inclusive).")
print("Can you guess it within 3 attempts? Make a try.")

no_of_attempts = 0
guess = False
user_input = 0 #an initial value
while no_of_attempts < 3:
    #user's input
    user_input = int(input("Enter Your answer."))
    no_of_attempts += 1
    if user_input == picked_number:
        guess = True
        break
    elif user_input > picked_number:
        print("It's high. Try again!")
    
    else:
        print("It's low. Try again!")

if guess:
    print("Excellent. You have guessed it right.")
    print(f"you've taken {no_of_attempts} attempt(s).")
else:
    print(f"The computer picked the number:{picked_number}.")
    print("You have lost the game now!")
    