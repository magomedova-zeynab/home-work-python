class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.owner = owner
        self._balance = balance
        self._history = []

    def get_balance(self):
        return self._balance

    def get_history(self):
        return list(self._history)

    def _log(self, operation, amount):
        self._history.append((operation, amount, self._balance))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        self._log("deposit", amount)

    def _can_withdraw(self, amount):
        return amount <= self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if not self._can_withdraw(amount):
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._log("withdraw", amount)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, min_balance=100):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def _can_withdraw(self, amount):
        return self._balance - amount >= self.min_balance


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=1000):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def _can_withdraw(self, amount):
        return self._balance - amount >= -self.credit_limit


if __name__ == "__main__":
    accounts = [
        BankAccount("Иван", 1000),
        SavingsAccount("Мария", 2000, min_balance=500),
        CreditAccount("Петр", 500, credit_limit=1000),
    ]

    for acc in accounts:
        try:
            acc.withdraw(1200)
            print(f"{acc.owner}: снято 1200, баланс {acc.get_balance()}")
        except ValueError as e:
            print(f"{acc.owner}: {e}")

    for acc in accounts:
        print(acc.owner, acc.get_balance(), acc.get_history())