class BankAccount:

    def __init__(self, initial_balance: int) -> None:
        self._balance: int = initial_balance

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        self._balance -= amount

    def get_balance(self) -> int:
        return self._balance


if __name__ == "__main__":
    account: BankAccount = BankAccount(100)
    print(account.get_balance())
    account.deposit(100)
    print(account.get_balance())
    account.withdraw(1000)
    print(account.get_balance())
    account.deposit(-1000)
    print(account.get_balance())
    account.withdraw(-1000)
    print(account.get_balance())
