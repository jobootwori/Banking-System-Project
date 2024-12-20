# src/main.py

def display_menu():
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Please select an option (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_balance(balance):
    print(f"Your current account balance is: ${balance:.2f}")

def deposit(balance):
    while True:
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
                break
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return balance

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"${amount:.2f} withdrawn successfully.")
                    break
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return balance

def banking_system():
    account_balance = 1000.0
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            check_balance(account_balance)
        elif choice == 2:
            account_balance = deposit(account_balance)
        elif choice == 3:
            account_balance = withdraw(account_balance)
        elif choice == 4:
            print("Thank you for using our banking system. Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Basic Banking System!")
    banking_system()
