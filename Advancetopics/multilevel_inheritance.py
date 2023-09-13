class Grandfather():
    def fun1(self):
        print("grand father")

class Parent(Grandfather):
    def fun2(self):
        print("parent function")

class Child(Parent):
    def fun3(self):
        print("child function")

obj=Child()
obj.fun1()
obj.fun2()
obj.fun3()
