class BitIterator:
    def __init__(self, n):
        self.n = n

    def next(self):
        if self.n == 0:
            raise StopIteration()
        else:
            t = self.n % 2
            self.n = self.n / 2
            return t

class Integer:
    def __init__(self, n):
        self.n = n

    def __iter__(self): 
        return BitIterator(self.n)



        
k = Integer(255)

for bit in k:
    print bit


