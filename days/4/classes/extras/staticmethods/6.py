import time

class Date:
    def __init__(self):
        t = time.localtime()
        self.year = t.tm_year
        self.month = t.tm_mon
        self.day = t.tm_mday


d = Date()


