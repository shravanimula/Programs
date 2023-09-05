class Variable:
    a=10 #static variable
    def __init__(self):
        self.b=20 #instance variable
         

a1=Variable()
a2=Variable()
print("a1:",a1.a,a1.b)
print("a2:",a2.a,a2.b)
Variable.a=99
a1.b=45
print("a1:",a1.a,a1.b)
print("a2:",a2.a,a2.b)
