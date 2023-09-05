class Test:
    def __init__(self):
        self.a=10
    def m1(self):
       self.b=20

variable=Test()
variable.m1()
variable.c=30
print(variable.__dict__)
