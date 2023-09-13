class Parent():
    def fun(self):
        print("parent function")

class Child(Parent):
    def fun1(self):
        print("child function")

obj=Child()
obj.fun()
obj.fun1()
