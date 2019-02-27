class cal(object):
    count = 0
    str = ''
    val = []


    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def add(self):
        result = self.v1 + self.v2
        cal.val.append("%d+%d=%d" %(self.v1, self.v2,result))

    def show(self):
        for v in cal.val:
            print(v)

    # decorator 자바에서의 어노테이션과는 다르다.
    @staticmethod
    def method1():
        print('static method')

    @classmethod
    def method2(self):
        print('class method')


c1= cal(2,3)
c1.add()
c1.add()
c1.show()

c1.method1()