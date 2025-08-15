# can be manually throw an exception using raise when you detect an invalid condition in your code.
# used for input validation and custom error signaling
# can raise built in exceptions

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError('Insufficient funds')
    return balance - amount

try:
    new_balance = withdraw(100, 300)
except ValueError as e:
    print(f'Error: {e}')