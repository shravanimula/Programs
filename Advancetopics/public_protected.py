class A:
    def __init__(self,a,b):
        self.a=a
        self._b=b

class B:
    def fun():
        obj=A(10,20)
        print("public a:",obj.a)
        print("private b:",obj._b)

B.fun()
