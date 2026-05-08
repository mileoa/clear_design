class BankAccount:

    def __init__(self, initial_balance: int) -> None:
        if initial_balance < 1:
            raise ValueError("initial_balance must be >= 1")
        self._balance: int = initial_balance

    def deposit(self, amount: int) -> None:
        if amount < 1:
            raise ValueError("amount must be >= 1")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount < 1:
            raise ValueError("amount must be >= 1")
        new_balance: int = self._balance - amount
        if new_balance < 0:
            raise ValueError("this action will result in a negative amount")
        self._balance = new_balance

    def get_balance(self) -> int:
        return self._balance


if __name__ == "__main__":
    try:
        account: BankAccount = BankAccount(-100)
    except Exception as e:
        pass
    try:
        account: BankAccount = BankAccount(100)
    except Exception as e:
        pass
    print(account.get_balance())

    account.deposit(100)
    print(account.get_balance())

    try:
        account.withdraw(1000)
    except Exception as e:
        pass
    print(account.get_balance())

    try:
        account.deposit(-1000)
    except Exception as e:
        pass

    print(account.get_balance())

    try:
        account.withdraw(-1000)
    except Exception as e:
        pass
    print(account.get_balance())
