
class A:
    def fun1(self):
        print 'A: fun1'

class B:
    def fun2(self):
        print 'B: fun2'

class C(A, B):
    def fun3(self):
        print 'C: fun3'


t = C()
t.fun3()
t.fun2()
t.fun1()

