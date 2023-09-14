class Parent:
    def fun(self):
        print("iam in parent")

class Child(Parent):
    def fun(self):
        super().fun()
        print("iam in child")

    def fun2(self):
        self.fun()

obj=Child()
obj.fun2()
