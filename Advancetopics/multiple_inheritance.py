class Parent1:
    def fun(self):
        print("I am in parent1:")

class Parent2():
    def fun1(self):
        print("i am in parent2")

class Child(Parent1,Parent2):
    def fun2(self):
        print("iam in child")

obj=Child()
obj.fun()
obj.fun1()
obj.fun2()
