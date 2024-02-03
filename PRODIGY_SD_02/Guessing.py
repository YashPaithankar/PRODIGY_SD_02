import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Number of attempts allowed
    max_attempts = 5
    
    print("Welcome to the Guess the Number game!")
    print(f"Try to guess the secret number between 1 and 100. You have {max_attempts} attempts.")

    # Loop for the number of attempts
    for attempt in range(1, max_attempts + 1):
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
guess_the_number()
