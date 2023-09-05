class Variable:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        print("within the class")
        print(self.a)
        print(self.b)

data=Variable()
data.m1()
print("outside of the class")
print(data.a)
print(data.b)
