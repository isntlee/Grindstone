from transactions import Deposit, Withdrawal, OpenAccount


class BankAccount:
    def __init__(self, customerId, name, balance):
        self._customerId = customerId
        self._name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


class AccountSystem:
    def __init__(self, accounts, transactions):
        self._accounts = accounts
        self._transactions = transactions

    def get_account(self, customerId):
        return self._accounts[customerId]

    def get_accounts(self):
        return self._accounts

    def get_transactions(self):
        return self._transactions

    def open_account(self, customer_name, teller_id):
        # Create account
        customerId = len(self.get_accounts())
        account = BankAccount(customerId, customer_name, 0)
        self._accounts.append(account)

        # Log transaction
        transaction = OpenAccount(customerId, teller_id)
        self._transactions.append(transaction)
        return customerId

    def deposit(self, customer_id, teller_id, amount):
        account = self.get_account(customer_id)
        account.deposit(amount)

        transaction = Deposit(customer_id, teller_id, amount)
        self._transactions.append(transaction)

    def withdraw(self, customer_id, teller_id, amount):
        if amount > self.get_account(customer_id).get_balance():
            raise Exception('Insufficient funds')
        account = self.get_account(customer_id)
        account.withdraw(amount)

        transaction = Withdrawal(customer_id, teller_id, amount)
        self._transactions.append(transaction)
