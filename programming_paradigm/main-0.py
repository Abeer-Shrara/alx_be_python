import sys
from bank_account import BankAccount

def main():
    # Create an account with $100 to start
    account = BankAccount(100)

    # Check if the user typed a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Example: "deposit:50" → command = "deposit", amount = 50
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # If command = deposit
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    # If command = withdraw
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    # If command = display
    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
