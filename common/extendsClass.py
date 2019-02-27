class test3(object):
    def __init__(self,v):
        self.value = v
    
    def show(self):
        print(self.value*2)


class test2(test3):
    def show(self):
        print(self.value*3)

c1=test3(5) 
c1.show()

c2 =test2(4)
c2.show()
 

