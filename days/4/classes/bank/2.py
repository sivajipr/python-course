
def new_account():
    return {'balance' : 0}

def deposit(account, amount):
    account['balance'] += amount

def withdraw(account, amount):
    account['balance'] -= amount

def check_balance(account):
    return account['balance']


acc1 = new_account()
print acc1

deposit(acc1, 100)
print acc1

acc2 = new_account()
print acc2

deposit(acc2, 200)
print acc2
