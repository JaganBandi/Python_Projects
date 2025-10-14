# Number Guessing Game using if-else-while

secret_number = 7  # The number to guess
guess = None       # Variable to store user guess

while guess != secret_number:  # Loop until correct guess
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
    else:
        print("❌ Wrong guess. Try again!")

print("Game Over.")
