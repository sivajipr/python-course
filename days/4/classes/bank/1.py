balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

def check_balance():
    return balance

deposit(100)
print check_balance()

withdraw(200)
print check_balance()

