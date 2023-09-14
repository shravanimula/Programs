class Parent:
    def fun1(self):
        print("I am in parent1:")

class Child1(Parent):
    def fun2(self):
        print("i am in child1")

class Child2(Parent):
    def fun3(self):
        print("iam in child2")

obj1=Child1()
obj2=Child2()
obj1.fun1()
obj1.fun2()
obj2.fun3()
obj2.fun1()

