a=10
class Test:
    a=20
    def fun():
        print("global value of a is:",a)
        print("class variable of a is:",Test.a)

Test.fun()
