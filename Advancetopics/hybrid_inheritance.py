class Parent:
    def fun1(self):
        print("iam in parent ")

class Child1(Parent):
    def fun2(self):
        print("iam in child1 ")

class Child2(Parent):
    def fun3(self):
        print("iam in child2 ")

class Child3(Child1,Child2):
    def fun4(self):
        print("iam in child3")


obj=Child3()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()
