class Variable:
     def __init__(self):
         self.a=10
         self.b=20
         self.c=30
     def fun1(self):
         del self.a
        
a1=Variable()
a2=Variable()
print(a1.__dict__)
print(a2.__dict__)
a1.fun1()
del a2.b
a1.c=44
print(a1.__dict__)
print(a2.__dict__)
