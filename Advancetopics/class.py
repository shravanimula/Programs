class A:
    def __init__(self):
        print("constructor")
    def fun1(self):
        print("class method")
    class B:
        def __init__(self):
            print("Inner class constructor")
        def fun2(self):
            print("Inner class method")


a=A()
a.fun1()
b=a.B()
b.fun2()
