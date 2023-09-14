class Grandfather:
    def fun(self):
        print("iam in grandfather")

class Parent(Grandfather):
    def fun(self):
        print("iam in Parent")

class Child(Parent):
    def fun(self):
        print("iam in child")

    def display(self):
        self.fun()
        super(Child,self).fun()
        super(Parent,self).fun()

obj=Child()
obj.display()
