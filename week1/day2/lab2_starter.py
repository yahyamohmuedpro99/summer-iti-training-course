class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    pass


# Example Usage
# myacc_savings = SavingsAccount("Someone", 1000)
# myacc_savings.deposit(500)
# myacc_savings.apply_interest(0.05)
# myacc_savings.withdraw(300)
# print(myacc_savings) #  Account owner: SomeoneAccount balance: 1500.0

# myacc_checking = CheckingAccount("SomeoneElse", 200)
# myacc_checking.deposit(100)
# myacc_checking.withdraw(50)
# print(myacc_checking) # Account owner: SomeoneElse\nAccount balance: 150.0"}


