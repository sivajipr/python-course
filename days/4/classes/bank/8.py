class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def check_balance(self):
        return self.balance

acc1 = Account(1000)
acc1.deposit(100)
print acc1.check_balance()

acc2 = Account()
acc2.deposit(200)
print acc2.check_balance()
