class BankAccount:
    def __init__(self, initial_balance=0):
        # Every account starts with some money (default = 0)
        self.__account_balance = initial_balance   # private variable (hidden)

    def deposit(self, amount):
        # Add money
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        # Take out money (only if enough money is there)
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True   # success
        return False      # fail (not enough money)

    def display_balance(self):
        # Show how much money is left
        print(f"Current Balance: ${self.__account_balance}")
