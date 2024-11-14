from random import randint


def number_guess():
    number = randint(1, 100)
    attempts = 0  # Track the number of attempts
    print("Welcome to the Number Guessing Game!")

    while True:
        user_input = input("Enter your guess (or type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break

        try:
            user_guess = int(user_input)
            attempts += 1  # Increment attempts

            if user_guess > number:
                print("Too high!")
            elif user_guess < number:
                print("Too low!")
            else:
                print(f"Congrats! You guessed the correct number {number} in {attempts} attempts!")
                break  # Exit the loop on correct guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


number_guess()