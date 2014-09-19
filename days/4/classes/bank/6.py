class Account:
    def __init__(self, balance):
        self.balance = balance

def deposit(acct, amt):
    acct.balance += amt

def withdraw(acct, amt):
    acct.balance -= amt

def check_balance(acct):
    return acct.balance

acc1 = Account(1000)
deposit(acc1, 100)
print check_balance(acc1)

acc2 = Account()
deposit(acc2, 200)
print check_balance(acc2)
