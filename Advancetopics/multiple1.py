class A():
    def f1(self):
        print(" I am in class A")

class B():
    def f2(self):
        print("I am in class B")
        
class C(A,B):
    def f3(self):
        print("I am in class C")

a=C()
a.f1()
a.f2()
a.f3()
