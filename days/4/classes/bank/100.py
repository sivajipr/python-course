class Account:
    def __init__(self):
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount

 
    def check_balance(self):
        return self.balance


acc1 = Account()
acc1.deposit(100)
print acc1.check_balance()

acc2 = Account()
acc2.deposit(200)
print acc2.check_balance()
