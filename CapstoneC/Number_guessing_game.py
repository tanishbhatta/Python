""" 
Number Guessing Game - Capstone 5 (Tanish Bhatta)

Requirements:
1) Program picks a random integer
2) User guesses repeatedly with higher/lower hints
3) Tracks attempt count
4) Input validation loop — alphabetical input must not crash the program
5) Replay with cumulative score tracking 

"""
import random

print("Number Guessing Game".center(45, '-'))

#pre-deciding
total_games_played = 0
total_games_won = 0
cumulative_burned_attempts = 0

while True:

    victory = False

    while True:
        raw_lower = input("\nEnter the lower bound: ").strip()

        if raw_lower.isdigit():
            lower = int(raw_lower)
            break
        else:
            print("\n\tInvalid Token: Enter a positive integer")
    
    while True:
        raw_upper = input("Enter the upper bound: ").strip()

        if raw_upper.isdigit():
            upper = int(raw_upper)
            if upper > lower:
                break
            print(f"\n\tInvalid: Upper bound must be greater than the lower {lower}")
        else:
            print("\n\tInvalid Token: Enter a positive integer")

    num = random.randint(lower, upper)
    attempt = 0

    print("\nYou have 7 guesses")

    while attempt < 7:

        while True:
            raw_guess = input(f"\n[Attempt {attempt+1}] Guess a number: ").strip()

            if raw_guess.isdigit():
                guess = int(raw_guess)
                break
            else:
                print("\n\tInvalid Token: Enter a positive integer")
        
        if guess > num:
            print("\n\tTarget Status: Lower!")
            attempt += 1
        elif guess < num:
            print("\n\tTarget Status: Higher!")
            attempt += 1
        else:
            print(f"\n\t\tCorrect! You guessed the number in {attempt} attempts")
            victory = True
            break
    
    total_games_played += 1
    cumulative_burned_attempts += attempt

    if victory:
        total_games_won += 1
    else:
        print(f"\n\t\tLost: the number was {num}")

    print(f"""\n
{"-"*45}
\t\tScoreboard
{"-"*45}
Total Games Played: {total_games_played}
Burned Attempts: {cumulative_burned_attempts}
Total Games Won: {total_games_won}
{"-"*45}
""")
    
    while True:
        again = input("\nDo you want to play again? (y/n): ").strip().lower()

        if again == "y":
            break
        elif again == "n":
            exit()
        else:
            print("\n\tInvalid Token: Enter y/n")
            continue

    
    



