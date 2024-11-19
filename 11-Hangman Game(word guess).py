import random

def hangman():
    wordlist = ["Universe", "Life", "Magic", "Entropy", "Change", "Love", "Manifestation"]
    selected_word = random.choice(wordlist).lower()  # Select a random word
    current_state = "_" * len(selected_word)  # Initialize current state
    attempts = 6  # Set maximum attempts

    print(f"The word is: {current_state}")
    print(f"You have {attempts} attempts left.")

    while attempts > 0 and current_state != selected_word:
        user_guess = input("Guess a letter: ").lower()  # Get user guess

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single letter.")
            continue  # Skip to the next iteration if input is invalid

        if user_guess in selected_word:  # Check if guess is correct
            # Update current state
            current_state_list = list(current_state)  # Convert to list for mutability
            for i in range(len(selected_word)):
                if selected_word[i] == user_guess:
                    current_state_list[i] = user_guess  # Update correct positions
            current_state = ''.join(current_state_list)  # Convert back to string
            print(f"Good guess! The word is now: {current_state}")
        else:
            attempts -= 1  # Decrement attempts if guess is wrong
            print(f"Incorrect guess! You have {attempts} attempts left.")

        # Check for win/loss after processing the guess
        if current_state == selected_word:
            print("Congratulations! You've guessed the word!")
            break  # Exit the loop if the word is guessed
    else:
        # If the loop ends without a win, the player loses
        print(f"Sorry, you've run out of attempts. The word was: {selected_word}.")

# Start the game
if __name__ == "__main__":
    hangman()

