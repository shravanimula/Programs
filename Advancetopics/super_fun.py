#super function call allows to call a parent method from the child
class Parent:
    def fun1(self):
        print("i am in parent")

class Child(Parent):
    def fun2(self):
        super().fun1()
        print("iam in child")

obj=Child()
obj.fun2()
