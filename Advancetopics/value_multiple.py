class Parent1:
    def __init__(self,a):
        self.parentvalue1=a

class Parent2:
    def __init__(self,b):
        self.parentvalue2=b

class Child(Parent1,Parent2):
    def __init__(self,a,b,c):
        Parent1.__init__(self,a)
        Parent2.__init__(self,b)
        self.childvalue=c

    def printvalue(self):
        print("a value is:",self.parentvalue1)
        print("b value is:",self.parentvalue2)
        print("c value is:",self.childvalue)

obj=Child(10,20,30)
obj.printvalue()
