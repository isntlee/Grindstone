import random
from accounts import AccountSystem


class Bank:
    def __init__(self, branches, bank_system, total_cash):
        self._branches = branches
        self._bank_system = bank_system
        self._total_cash = total_cash

    def add_branch(self, address, initial_funds):
        branch = BankBranch(address, initial_funds, self._bank_system)
        self._branches.append(branch)
        return branch

    def collect_cash(self, ratio):
        for branch in self._branches:
            cash_collected = branch.collect_cash(ratio)
            self._total_cash += cash_collected

    def print_transactions(self):
        for transaction in self._bank_system.get_transactions():
            print(transaction.get_transaction_description())


class BankBranch:
    def __init__(self, address, cash_on_hand, bank_system):
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._bank_system = bank_system
        self._tellers = []

    def add_teller(self, teller):
        self._tellers.append(teller)

    def _get_available_teller(self):
        index = round(random.random() * (len(self._tellers) - 1))
        return self._tellers[index].get_id()

    def open_account(self, customer_name):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        teller_id = self._get_available_teller()
        return self._bank_system.open_account(customer_name, teller_id)

    def deposit(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        teller_id = self._get_available_teller()
        self._bank_system.deposit(customer_id, teller_id, amount)

    def withdraw(self, customer_id, amount):
        if amount > self._cash_on_hand:
            raise ValueError('Branch does not have enough cash')
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        self._cash_on_hand -= amount
        teller_id = self._get_available_teller()
        self._bank_system.withdraw(customer_id, teller_id, amount)

    def collect_cash(self, ratio):
        cash_to_collect = round(self._cash_on_hand * ratio)
        self._cash_on_hand -= cash_to_collect
        return cash_to_collect

    def provide_cash(self, amount):
        self._cash_on_hand += amount


class BankEmployee:
    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id
    

bankSystem = AccountSystem([], [])
bank = Bank([], bankSystem, 10000)

branch1 = bank.add_branch('123 Main St', 1000)
branch2 = bank.add_branch('456 Elm St', 1000)

branch1.add_teller(BankEmployee(1))
branch1.add_teller(BankEmployee(2))
branch2.add_teller(BankEmployee(3))
branch2.add_teller(BankEmployee(4))

customerId1 = branch1.open_account('John Doe')
customerId2 = branch1.open_account('Bob Smith')
customerId3 = branch2.open_account('Jane Doe')

branch1.deposit(customerId1, 100)
branch1.deposit(customerId2, 200)
branch2.deposit(customerId3, 300)

branch1.withdraw(customerId1, 50)
""" Possible Output:
    Teller 1 opened account 0
    Teller 2 opened account 1
    Teller 3 opened account 2
    Teller 1 deposited 100 to account 0
    Teller 2 deposited 200 to account 1
    Teller 4 deposited 300 to account 2
    Teller 2 withdrew 50 from account 0
"""

bank.print_transactions()
