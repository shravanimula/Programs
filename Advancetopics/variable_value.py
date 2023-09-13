#modify the value of variable in the method

class Test:
    a=10
    def fun1():
        print("in fun1 the value of a is:",Test.a)
        Test.a=Test.a+100
        Test.fun2()

    def fun2():
        print("in fun2 the value of a is:",Test.a)

Test.fun1()
