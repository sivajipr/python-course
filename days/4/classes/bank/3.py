class Account:
    pass

def new_account():
    a = Account()
    a.balance = 0
    return a

def deposit(acct, amt):
    acct.balance += amt

def withdraw(acct, amt):
    acct.balance -= amt

def check_balance(acct):
    return acct.balance

acc1 = new_account()
deposit(acc1, 100)
print check_balance(acc1)

acc2 = new_account()
deposit(acc2, 200)
print check_balance(acc2)
