class Parent:
    a=10
    _b=20
    __c=30

class Child(Parent):
    print(Parent.a)
    print(Parent._b)

a1=Child()
