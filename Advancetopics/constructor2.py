class Parent:
    def __init__(self,b):
        self.b=b
        print("in parent :", self.b)
        
class Child(Parent):
    def __init__(self,a,b):
        Parent.__init__(self,b)
        self.a=a
        

obj=Child(10,100)
print("parent b value is:",obj.b)
print("child a value is :",obj.a)
