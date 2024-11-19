class BankAccount:
    def __init__(self, username, initial_balance):
        """
        Initialize a new bank account with a username and initial balance.

        Parameters:
        username (str): The name of the account holder.
        initial_balance (float): The starting balance of the account.
        """
        self.username = username  # Store the username
        self.balance = initial_balance  # Store the initial balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Parameters:
        amount (float): The amount to deposit.
        """
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount  # Increase the balance
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")  # Inform user if amount is invalid

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.balance:  # Check if the amount is valid and sufficient
            self.balance -= amount  # Decrease the balance
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")  # Inform user if withdrawal fails

    def check_balance(self):
        """Display the current balance of the account."""
        print(f"Current balance: {self.balance}")  # Print the balance


def main():
    """Main function to run the banking application."""
    account = None  # Initialize account variable

    while True:  # Start an infinite loop for user interaction
        # Display menu options to the user
        print("\nWelcome to the Simple Banking System!")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Choose an option: ")  # Get user input

        if choice == '1':  # Option to create an account
            username = input("Enter your username: ")  # Prompt for username
            initial_balance = float(input("Enter initial balance: "))  # Prompt for initial balance
            account = BankAccount(username, initial_balance)  # Create a new BankAccount instance
            print(f"Account created for {username} with balance: {initial_balance}")

        elif choice == '2':  # Option to deposit money
            if account is None:  # Check if an account exists
                print("You need to create an account first.")  # Inform user to create an account
            else:
                amount = float(input("Enter amount to deposit: "))  # Prompt for deposit amount
                account.deposit(amount)  # Call deposit method

        elif choice == '3':  # Option to withdraw money
            if account is None:  # Check if an account exists
                print("You need to create an account first.")  # Inform user to create an account
            else:
                amount = float(input("Enter amount to withdraw: "))  # Prompt for withdrawal amount
                account.withdraw(amount)  # Call withdraw method

        elif choice == '4':  # Option to check balance
            if account is None:  # Check if an account exists
                print("You need to create an account first.")  # Inform user to create an account
            else:
                account.check_balance()  # Call check_balance method

        elif choice == '5':  # Option to exit the application
            print("Goodbye!")  # Print goodbye message
            break  # Exit the loop

        else:  # Handle invalid input
            print("Invalid option. Please try again.")  # Inform user of invalid option


# Start the application
if __name__ == "__main__":
    main()      # Call the main function to run the application