class Parent():
    def fun():
        print("parent function")

class Child(Parent):
    def fun1():
        print("child function")

Child.fun()
Child.fun1()
