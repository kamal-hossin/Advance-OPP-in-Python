class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # protected attribute

    # Getter using property decorator
    @property
    def balance(self):
        return self._balance

    # Setter using decorator
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Invalid balance!")

    # Read-only property
    @property
    def account_type(self):
        return "Savings Account"


Brac_bank = BankAccount("Kamal", 5000)
print("Balance:", Brac_bank.balance)
Brac_bank.balance = 9000
print("Updated Balance:", Brac_bank.balance)
print("Account Type:", Brac_bank.account_type)
Brac_bank.balance = -100