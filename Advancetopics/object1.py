class Test:
    a=20
    def __init__(self,a):
        self.var=a
        print("in constructor :",self.var)
    def printfun(self):
        a=30
        print("in print fun a is:",a)
        print("in object of a :",self.var)
        print("in class a :",Test.a)

obj=Test(10)
obj.printfun()
