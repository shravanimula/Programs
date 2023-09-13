#class level method (func()) can be accessed using class name

class Test:
    a=10
    print("inside the class :",a)
    def func():
        print("in function that value of a is:",Test.a)

Test.func()
print("outsuide the class:",Test.a)
