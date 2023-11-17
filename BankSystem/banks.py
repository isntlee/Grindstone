import random


class Bank:
    def __init__(self, branches, account_system, total_cash):
        self._branches = branches
        self._account_system = account_system
        self._total_cash = total_cash

    def add_branch(self, address, initial_funds):
        branch = BankBranch(address, initial_funds, self._account_system)
        self._branches.append(branch)
        return branch

    def collect_cash(self, ratio):
        for branch in self._branches:
            cash_collected = branch.collect_cash(ratio)
            self._total_cash += cash_collected

    def print_transactions(self):
        for transaction in self._account_system.get_transactions():
            print(transaction.get_transaction_description())


class BankBranch:
    def __init__(self, address, cash_on_hand, account_system):
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._account_system = account_system
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
        return self._account_system.open_account(customer_name, teller_id)

    def deposit(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        teller_id = self._get_available_teller()
        self._account_system.deposit(customer_id, teller_id, amount)

    def withdraw(self, customer_id, amount):
        if amount > self._cash_on_hand:
            raise ValueError('Branch does not have enough cash')
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        self._cash_on_hand -= amount
        teller_id = self._get_available_teller()
        self._account_system.withdraw(customer_id, teller_id, amount)

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
