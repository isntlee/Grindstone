from accounts import AccountSystem
from banks import Bank, BankEmployee


accountSystem = AccountSystem([], [])
bank = Bank([], accountSystem, 10000)

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