class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма снятия должна быть положительной")
    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств на счёте")
    return balance - amount


try:
    new_balance = withdraw(1000, 1500)
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")