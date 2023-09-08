class Parent():
    name="aaaa"
    age=33

class Child(Parent):
        child_name="bbbbb"
        child_age=2

var=Child()
print(var.child_name)
print(var.child_age)
print(var.name)
print(var.age)
