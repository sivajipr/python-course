
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def check_balance(self):
        return self.balance

class LimitedAccount(Account):
    def withdraw(self, amt):
        if (self.balance - amt) < 0:
            print 'Balance is only %d' % self.balance
            print 'Can not withdraw %d' % amt  
        else:
            self.balance -= amt

acc1 = LimitedAccount(100)
acc1.withdraw(200)
