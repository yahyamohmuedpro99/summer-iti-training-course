"""
Problem: Banking System
Description:

    Design a simple banking system using OOP principles. 
    The system should manage different types of accounts, 
    such as checking and savings accounts.
    Each account should support basic operations like deposits, 
    withdrawals, and checking balances. 
    In addition, different types of accounts might have different rules or behaviors.

Requirements:

Account Class:

Account should be a base class with:
An account_number
An owner (name of the account holder)
A balance
Methods for deposit, withdraw, and get_balance.
CheckingAccount Class:

Inherit from Account.
Add a transaction_fee attribute that is deducted from each withdrawal.
Override the withdraw method to include the transaction fee.
SavingsAccount Class:

Inherit from Account.
Add an interest_rate attribute.
Add a method apply_interest to apply interest to the balance periodically.
Bank Class:

Manage multiple accounts.
Methods to add_account, find_account, and transfer_funds between accounts.

"""

# ------------------------------------
# -------------- OOP -----------------
# ------------------------------------
class Account:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance


class CheckingAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, transaction_fee=1.00):
        super().__init__(account_number, owner, initial_balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_withdrawal = amount + self.transaction_fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrew ${amount} with a transaction fee of ${self.transaction_fee}. New balance: ${self.balance}.")
        else:
            print("Insufficient funds including transaction fee.")


class SavingsAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: ${interest}. New balance: ${self.balance}.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added.")

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount} from account {from_account_number} to account {to_account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

# Example usage
bank = Bank()

acc1 = CheckingAccount("001", "Alice", 1000)
acc2 = SavingsAccount("002", "Bob", 5000)

bank.add_account(acc1)
bank.add_account(acc2)

acc1.deposit(200)
acc1.withdraw(150)
acc2.apply_interest()

bank.transfer_funds("001", "002", 100)

# ------------------------------------
# ----------- Functions --------------
# ------------------------------------
# Define account data structures
accounts = {
    "001": {"owner": "Alice", "balance": 1000, "type": "checking", "transaction_fee": 1.00},
    "002": {"owner": "Bob", "balance": 5000, "type": "savings", "interest_rate": 0.01}
}

def deposit(account_number, amount):
    if account_number in accounts:
        if amount > 0:
            accounts[account_number]["balance"] += amount
            print(f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}.")
        else:
            print("Deposit amount must be positive.")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        account = accounts[account_number]
        if amount > 0:
            if account["type"] == "checking":
                total_withdrawal = amount + account["transaction_fee"]
                if total_withdrawal <= account["balance"]:
                    account["balance"] -= total_withdrawal
                    print(f"Withdrew ${amount} with a transaction fee of ${account['transaction_fee']}. New balance: ${account['balance']}.")
                else:
                    print("Insufficient funds including transaction fee.")
            else:  # Savings account
                if amount <= account["balance"]:
                    account["balance"] -= amount
                    print(f"Withdrew ${amount}. New balance: ${account['balance']}.")
                else:
                    print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    else:
        print("Account not found.")

def get_balance(account_number):
    if account_number in accounts:
        return accounts[account_number]["balance"]
    else:
        print("Account not found.")
        return None

def apply_interest(account_number):
    if account_number in accounts and accounts[account_number]["type"] == "savings":
        account = accounts[account_number]
        interest = account["balance"] * account["interest_rate"]
        account["balance"] += interest
        print(f"Applied interest: ${interest}. New balance: ${account['balance']}.")
    else:
        print("Account not found or not a savings account.")

def transfer_funds(from_account_number, to_account_number, amount):
    if from_account_number in accounts and to_account_number in accounts:
        from_account = accounts[from_account_number]
        to_account = accounts[to_account_number]
        if amount > 0:
            if from_account["balance"] >= amount:
                withdraw(from_account_number, amount)
                deposit(to_account_number, amount)
                print(f"Transferred ${amount} from account {from_account_number} to account {to_account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")
    else:
        print("One or both accounts not found.")

# Example usage
deposit("001", 200)
withdraw("001", 150)
apply_interest("002")
transfer_funds("001", "002", 100)

