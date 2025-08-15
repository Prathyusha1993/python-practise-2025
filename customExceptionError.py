# we can create own exception types by inheriting from python's exception class

# why use custom exceptions: make your code more readable
# allow specific exception handling instead of catching all errors.
# useful i nlarge systems for error categorization

class InsufficientFundsError(Exception):
    """custom exception for insufficient funds."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError('Not enough balance in the account')
    return balance - amount


try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f'Custom exception error caught: {e}')