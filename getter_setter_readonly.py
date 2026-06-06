class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Private Attribute

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Setter Method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Balance")

    # Read Only Property
    @property
    def account_type(self):
        return "Savings Account"


# Object Create
acc1 = BankAccount("Kamal", 5000)

# Getter
print("Balance:", acc1.get_balance())

# Setter
acc1.set_balance(8000)

print("Updated Balance:", acc1.get_balance())

# Read Only
print("Account Type:", acc1.account_type)