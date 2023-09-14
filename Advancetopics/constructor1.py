class Parent:
    def __init__(self):
        print("parent object is creataed")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("child object is created")

obj=Child()
