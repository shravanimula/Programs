class Parent():
    def fun1(self):
        print("iam in parent class")

class Child(Parent):
    def fun2(self):
        print("iam in child class")


var=Child()
var.fun1()
var.fun2()
