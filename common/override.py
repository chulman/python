class A(object):
    def show(self):  
        return 'A'


class B(A):
    def show(self):
        return super().show() + 'B'


a = A()
print(a.show())
b = B()
print(b.show())