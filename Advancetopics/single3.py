class A():
    def fun(self):
        print("i am in class A")

class B(A):
    def fun(self):
        A.fun(self)
        print("i am in class B")

a=B()
a.fun()
