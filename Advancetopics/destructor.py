class A:
    def __init__(self):
        print("constructor called")
        self.name="aaaa"
        print(self.name)
    def __del__(self):
        print("destructor called")

a=A()
del a
