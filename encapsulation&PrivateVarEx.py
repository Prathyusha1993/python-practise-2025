# encapsulation: restricting direct access to an aobject's data by keeping it hidden(private/protexted)
# and providing controlled access through methods.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        self._secret_code = 'XYZ'

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

acc = BankAccount(100)
print(acc.get_balance())
acc.deposit(50)
print(acc.get_balance())
print(acc._secret_code)      #access via name mangling