# 객체 사용 및 생성자

class Calculator(object):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def minus(self):
        return self.v1 - self.v2

    def divsion(self):
        return self.v1 / self.v2    

    def mul(self):
        return self.v1 * self.v2

c = Calculator(3,4)


print(c.add())
print(c.minus())
print(c.divsion())
print(c.mul())




# 캡슐화 및 get ,set

class A(object):
    def __init__(self,v):
        if isinstance(v,int):  
            self.value = v
    
    def show(self):
        print(x)
        print(self.value)

    def setValue(self,v):
        self.value = v

    def getValue(self):
        return self.value


c1 = A(4)

c1.show()
c1.setValue(5)
print(c1.getValue())
