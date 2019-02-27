class C1():
    def methodC1(self):
        print('C1')

class C2():
    def methodC2(self):
        print('C2')

class C3(C1,C2):
    def method(self):
        print('C3')


c = C3()
c.methodC1()
c.methodC2()
c.method()
