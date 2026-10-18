"""A minimal in-memory bank account demonstration."""


class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if not 0 < amount <= self.balance:
            raise ValueError("Amount must be positive and no more than the balance.")
        self.balance -= amount


def main():
    account = BankAccount()
    while True:
        print(f"\nBalance: {account.balance:.2f}")
        action = input("1) Deposit  2) Withdraw  3) Quit: ").strip()
        if action == "3":
            return
        try:
            amount = float(input("Amount: "))
            if action == "1":
                account.deposit(amount)
            elif action == "2":
                account.withdraw(amount)
            else:
                print("Invalid option.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
