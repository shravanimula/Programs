class Parent:
    def fun():
        print("iam in parent")

class Child(Parent):
    def fun1(self):
        print("iam in child fun1 method")

    def fun(self):
        print("iam in child in fun method")

obj=Child()
obj.fun1()
obj.fun()
