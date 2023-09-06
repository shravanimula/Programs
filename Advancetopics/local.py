class Student:
    def fun1(self):
        name="aaaa"
        print(name)
        #print(marks)

    def fun2(self):
        marks=56  #local to this method
        print(marks)
    

a=Student()
a.fun1()
a.fun2()
