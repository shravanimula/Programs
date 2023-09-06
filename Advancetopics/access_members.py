class A:
    a=10
    _b=20
    __c=30

    def __init__(self):
        print("constructor called")
        print(self.a)
        print(self._b)
        print(self.__c)


a1=A()
print(a1.a)
print(a1._b)
